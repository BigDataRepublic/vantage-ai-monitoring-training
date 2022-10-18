# Vantage AI Monitoring Training

This repository contains a basic Python app with some logging and monitoring configured.
In order to use this repo:
1. create a [Grafana Cloud](https://grafana.com) account
2. use the "Connect Data" button to set up hosted logs, and add the url to the `logs` section of the [config](agent.yaml)
3. use the "Connect Data" button to set up hosted Prometheus metrics, and add the connection details to the `metrics` section of the [config](agent.yaml)
4. run `docker-compose up --build`
5. play around with the [deployed app](http://localhost:8000/docs)
6. explore the logs and metrics on [Grafana](https://grafana.com)
