# Observe LLM applications PoC

This is a PoC about how to observe LLM applications.

## How to run

Create a Python virtual environment and enable it:
```sh
$ python -m venv .venv && source .venv/bin/activate
```

Install the requeriments:
```sh
$ pip install -r requirements.txt
```

Run the application:

```sh
opentelemetry-instrument --exporter_otlp_insecure=true \ 
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --service_name llmdemo \
    --exporter_otlp_traces_endpoint http://0.0.0.0:4317 --exporter_otlp_metrics_endpoint 0.0.0.0:4317 \
    python app.py
```

You also need a cluster with the OpenTelemetry operator installed and deploy the resources in the `otel-col.yaml` file. You need to forward the `4317` port to the one from the `OpenTelemetryCollector`.

You can also package the app and run it in the cluster but you will need to create an `Instrumentation` resource and specify a custom image where the `openllmetry` packages are installed.
