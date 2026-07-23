Title: An AI-Assisted Breakthrough in Mathematical Optimization: A Problem Dating back 30 Years, a 2.5-Hour

URL Source: http://medium.com/@kerger.p/an-ai-assisted-breakthrough-in-convex-optimization-an-optimization-problem-dating-back-30-years-a-db5c631119de

Published Time: 2026-07-15T01:57:48Z

Markdown Content:
[![Image 1: Phillip Kerger](https://miro.medium.com/v2/resize:fill:32:32/1*O2hLFsQ-fsk8lTFbjxzo9Q.jpeg)](https://medium.com/@kerger.p?source=post_page---byline--db5c631119de---------------------------------------)

5 min read

Jul 15, 2026

Advances in AI-driven research in math and computer science have caused some stir over the last year, most recently with [OpenAI’s proof of a longstanding mathematical conjecture.](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) As a PhD in applied math myself, these have always felt like flukes, and I was never able to get any AI models to contribute significantly to any of my work. That has changed completely, and I am stunned by the results OpenAI’s new GPT 5.6 Sol model has given me.

In a single 2.5-hour session, OpenAI’s 5.6 Sol model produced a proof that closes a significant gap in mathematical optimization theory that had been open since 1996, my entire lifetime.

I had some ideas for this problem (see below for the exact problem if you are interested!). I’ve worked on it sporadically over the last year when I found inspiration, but nothing ever panned out. Hearing about some successes of AI in math research, I tried working with GPT 5.4 and 5.5, going back and forth over long sessions to explore different approaches in vain. Other researchers in mathematical optimization over time have spent time on this problem, and only last year at a the ICCOPT conference I heard someone say “we have no idea” how to solve this.

After the release of GPT Sol 5.6, I used a _very_ long prompt, 10 pages long in my paper, similar in design to the one OpenAI recently used in its work on the cycle double cover conjecture. Two and a half hours later, without any intervention from my end, **Sol 5.6 had solved the problem in one shot**.

But of course, we all know that these models are fantastic at bullsh*tting, and producing things that pass the eye test for being correct while being utter nonsense. I went through the proof myself, and all seemed correct, but I could always be deceived. To be absolutely sure, an important tool comes into play: Lean. Lean is a is a programming language to formalize math and computationally verify mathematical proofs. Axioms, variables, logic, and all else needed for mathematics can be formalized and modeled in Lean, and thus proofs of mathematical statements can be checked with Lean. So, I formally verified the proof in Lean, and setting everything up, the check passed: Sol had genuinely solved the problem. A gap in our understanding that had been open for 30 years, just like that.

The paper and Lean verification are available on [GitHub](https://github.com/PhillipKerger/zero-order-bounds-lean-verification), along with the full 10-page prompt used and the [initial chat](https://chatgpt.com/share/6a55aa50-b484-83ea-85c0-c7e7b4bda41c) that led to the main result.

## Verification of Results with Lean

AI-generated mathematical arguments need to be treated carefully. Models are quite capable of producing something that reads like a proof, uses the right vocabulary, but might not be 100% correct in the end. There was already too much noise in research before current models arrived, and now there will be much more pressure on researchers to separate real results from plausible-looking ones. So, we are entering the era where formal verification in Lean is becoming much, much more valuable to identify real results quickly! Google and others are already building models that generate ideas via LLMs and then attempt to formally prove their results in Lean, to create a verifiable automatic math reseracher. For mathematical results that can reasonably be formalized, I think this kind of verification needs to become normal for anyone in the field, and should start being required by journals. A single prompt can now generate something resembling a paper, so we are going to need better ways of checking what is actually true.

## Get Phillip Kerger’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

Part of me still hopes I have missed something important. I don’t like the idea that an AI model solved something that I am an expert in, much much faster than I ever could have, if I ever would have been able to even do so at all. But having verified everything in Lean, well, it looks like it did.

So now the question is: how many problems are researchers currently working on that are one good prompt away from a solution?Maybe I was unusually lucky. But I no longer think that is the only plausible explanation. People working in mathematics, computer science, and related fields are in for a wild ride.

## About the Problem

For readers who want a little more technical detail: the result is a new lower bound for the oracle complexity of deterministic, possibly nonsmooth, zeroth-order convex optimization, with respect to dimension d. This is a formal way of asking how much information an algorithm needs in order to solve an optimization problem where only the outcome of evaluating the function can be observed. These types of function-value only problems arise across areas like simulation-based engineering design, hyperparameter tuning in machine learning, and any optimization based on physical measurements or human feedback, so these optimization problems have been well-studied. Consider for example choosing the temperature, pressure, and processing time that minimize the predicted cost of manufacturing a product, where a deterministic simulator returns the cost for any chosen settings.

For this problem we want to minimize a convex function of d variables, but the only thing an algorithm can do is choose points and ask for the value of the function there. How many such function evaluations are needed before it can solve the problem?

An algorithm of Protasov from 1996 uses on the order of d² function evaluations. So we knew that roughly d² evaluations were sufficient. But the best lower bound for the past three decades was only on the order of d: we only knew that fewer than roughly d evaluations could not be enough. So, can you find an algorithm that is better than Prosatov’s, and only needs d evaluations? Or can you show that no such algorithm can exist, and we can sleep well at night knowing that Protasov’s algorithm using d² evaluations is best possible?

The new result gives a _lower bound_ of d², up to logarithmic and constant factors, on the number of evaluations needed to solve these optimization problems. In this setting, that means the d² evaluations that Protasov’s method uses is essentially the best algorithm possible for these problems!

For full details, see the preprint pdf available[here](https://github.com/PhillipKerger/zero-order-bounds-lean-verification).

Press enter or click to view image in full size

![Image 2](https://miro.medium.com/v2/resize:fit:700/1*XiUWRTG2DYnddYXLqJdHTw.png)
