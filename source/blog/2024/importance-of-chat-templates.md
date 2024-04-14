# The importance of chat templates

:::{post} 2024-04-11
:::

A long time ago, when GPT-3.5 (without turbo) was current, LLMs were simply trained to complete texts.
When GPT-3.5-turbo was released, there was a small but essential change in the course of ChatGPT.
Now the LLM could not only complete texts but also "read and understand" multi turn conversations.
At the same time, there was also the option of using system prompts.

:::{figure} /\_static/img/blog-2024/chat-template.png
:width: 550px
:::

OpenAI has named the whole thing Chat API. They define the roles of system, user and assistant.
Below is an example of how such a conversation is created using the Python API
([source](https://platform.openai.com/docs/guides/text-generation)).

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
```

However, the basic function of the LLMs has not changed in the course of the ChatAPI.
They read texts and generate the next token.
So how are the different types of text entered into the LLM?

The answer is: Templates

## Templates

Templates consist of markup - similar to XML - to mark and separate the different areas.
The most popular template format is ChatML. It looks like this:

```text
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Who won the world series in 2020?<|im_end|>
<|im_start|>assistant
The Los Angeles Dodgers won the World Series in 2020.<|im_end|>
<|im_start|>user
Where was it played?<|im_end|>
<|im_start|>assistant
```

Another template format is that of Zephyr, which looks like this:

```text
<|system|>
You are a helpful assistant.</s>
<|user|>
Who won the world series in 2020?</s>
<|assistant|>
The Los Angeles Dodgers won the World Series in 2020.</s>
<|user|>
Where was it played?</s>
<|assistant|>
```

## How do we use and apply these templates?

In the case of Hugging Face Transformers models, the chat template can be saved in the `tokenizer_config.json` configuration file.
More specifically, they are saved as a jinja template under the name `chat_template`.
In the case of ChatML, it looks like this:

```text
{% for message in messages %}
  {% if message['role'] == 'user' %}
    {{ '<|user|>\n' + message['content'] + eos_token }}
  {% elif message['role'] == 'system' %}
    {{ '<|system|>\n' + message['content'] + eos_token }}
  {% elif message['role'] == 'assistant' %}
    {{ '<|assistant|>\n'  + message['content'] + eos_token }}
  {% endif %}
  {% if loop.last and add_generation_prompt %}
    {{ '<|assistant|>' }}
  {% endif %}
{% endfor %}
```

This template can then be applied with the
[`tokenizer.apply_chat_template()`](https://huggingface.co/docs/transformers/main/en/internal/tokenization_utils#transformers.PreTrainedTokenizerBase.apply_chat_template)
function. More about this on the Hugging Face [Templates for Chat Models](https://huggingface.co/docs/transformers/main/en/chat_templating) page.

## The importance of chat templates

To understand the meaning of chat templates, we can test how the LLMs behave if you simply leave out the template.
This is exactly what [Daniel Furman](https://github.com/daniel-furman) did on this
[GitHub issue conversation](https://github.com/EleutherAI/lm-evaluation-harness/issues/1098#issuecomment-1953068243):

:::{figure} /\_static/img/blog-2024/model-eval-template.png
:width: 550px

Qualitative comparison of different LLMs with and without the template.
Table by [Daniel Furman](https://github.com/daniel-furman) from this
[GitHub issue conversation](https://github.com/EleutherAI/lm-evaluation-harness/issues/1098#issuecomment-1953068243).
:::

The table clearly shows that the use of the (correct) template has a significant impact on the quality of the generated answers.
