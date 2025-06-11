# Langfuse

## Links

- [Doc](https://langfuse.com/docs)
- [Python v3 SDK (OTEL-based)](https://langfuse.com/docs/sdk/python/sdk-v3)
- [OTEL (OpenTelemetry)](https://opentelemetry.io/)

## Traces and Observations

The top level entity in Langfuse are traces. Each trace contains one or multiple observations.
Each observation can have one of the following variants:

- **Events** are the basic building blocks. They are used to track discrete events in a trace.
- **Spans** represent durations of units of work in a trace.
- **Generations** are spans used to log generations of AI models. They contain additional attributes about the model, the prompt, and the completion. For generations, token usage and costs are automatically calculated.

Observations can also be nested.

also see: [Traces and Observations](https://langfuse.com/docs/tracing-data-model#traces-and-observations)
