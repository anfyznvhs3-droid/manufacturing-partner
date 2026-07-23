param(
    [string]$Destination = (Join-Path (Get-Location) 'recursion-source-archive')
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
New-Item -ItemType Directory -Force -Path $Destination | Out-Null

$sources = @(
    @{ Name = 'cdc-prompt.pdf'; Url = 'https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf' },
    @{ Name = 'cdc-proof.pdf'; Url = 'https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf' },
    @{ Name = 'chat-initial-proof.html'; Url = 'https://chatgpt.com/share/6a55aa50-b484-83ea-85c0-c7e7b4bda41c' },
    @{ Name = 'chat-refinement.html'; Url = 'https://chatgpt.com/share/6a55ad10-7644-83ea-859e-5483d2e0dff0' },
    @{ Name = 'medium-article.md'; Url = 'https://medium.com/@kerger.p/an-ai-assisted-breakthrough-in-convex-optimization-an-optimization-problem-dating-back-30-years-a-db5c631119de'; FallbackUrl = 'https://r.jina.ai/http://medium.com/@kerger.p/an-ai-assisted-breakthrough-in-convex-optimization-an-optimization-problem-dating-back-30-years-a-db5c631119de' },
    @{ Name = 'zero-order-bounds-lean-verification-master.zip'; Url = 'https://github.com/PhillipKerger/zero-order-bounds-lean-verification/archive/refs/heads/master.zip' }
)

$manifest = @()
foreach ($source in $sources) {
    $path = Join-Path $Destination $source.Name
    try {
        Invoke-WebRequest -Uri $source.Url -OutFile $path -MaximumRedirection 5 -UserAgent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'
        $manifest += [pscustomobject]@{
            source_url = $source.Url
            saved_as = $source.Name
            status = 'downloaded'
            sha256 = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
            captured_utc = (Get-Date).ToUniversalTime().ToString('o')
            note = ''
        }
    }
    catch {
        $originalError = $_.Exception.Message
        if ($source.FallbackUrl) {
            try {
                Invoke-WebRequest -Uri $source.FallbackUrl -OutFile $path -MaximumRedirection 5 -UserAgent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0 Safari/537.36'
                $manifest += [pscustomobject]@{
                    source_url = $source.Url
                    saved_as = $source.Name
                    status = 'downloaded-via-fallback'
                    sha256 = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
                    captured_utc = (Get-Date).ToUniversalTime().ToString('o')
                    note = "Original response: $originalError; fallback: $($source.FallbackUrl)"
                }
                continue
            }
            catch {
                $originalError += "; fallback response: $($_.Exception.Message)"
            }
        }
        $manifest += [pscustomobject]@{
            source_url = $source.Url
            saved_as = $source.Name
            status = 'failed'
            sha256 = ''
            captured_utc = (Get-Date).ToUniversalTime().ToString('o')
            note = $originalError
        }
    }
}

$repoPath = Join-Path $Destination 'zero-order-bounds-lean-verification.git'
try {
    if (-not (Test-Path -LiteralPath $repoPath)) {
        git clone --mirror 'https://github.com/PhillipKerger/zero-order-bounds-lean-verification.git' $repoPath
    }
    $commit = git -C $repoPath rev-parse HEAD
    $manifest += [pscustomobject]@{
        source_url = 'https://github.com/PhillipKerger/zero-order-bounds-lean-verification'
        saved_as = 'zero-order-bounds-lean-verification.git/'
        status = 'mirrored'
        sha256 = $commit.Trim()
        captured_utc = (Get-Date).ToUniversalTime().ToString('o')
        note = 'Git commit SHA'
    }
}
catch {
    $manifest += [pscustomobject]@{
        source_url = 'https://github.com/PhillipKerger/zero-order-bounds-lean-verification'
        saved_as = 'zero-order-bounds-lean-verification.git/'
        status = 'failed'
        sha256 = ''
        captured_utc = (Get-Date).ToUniversalTime().ToString('o')
        note = $_.Exception.Message
    }
}

$manifest | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath (Join-Path $Destination 'manifest.json') -Encoding utf8
