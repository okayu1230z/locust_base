# Locust Base Repository

You can build the environment of the software you want to test performance based on this repository.

Locust is an OSS tool for performance testing of Web Applications and Web APIs.


> Locust is an easy to use, scriptable and scalable performance testing tool.
> You define the behaviour of your users in regular Python code, instead of being stuck in a UI or restrictive domain specific language.

[official document](https://docs.locust.io/en/stable/)

- Write test scenarios in plain old Python
- Distributed and scalable - supports hundreds of thousands of concurrent users
- Web-based UI
- Can test any system
- Hackable

There are other OSS tools such as JMeter by Java and k6 by js, but locust describes scenarios in Python.

## How to use

A sample application is provided in the implementation of this repository, so replace it with the application you want to test.

## Implemantation

Create a class that inherits HttpUser, and those with task annotation will be executed by Locust.

Specify the host to be tested in the `host` property.

```
    host = "http://127.0.0.1:5000"
```

The sample code points to the sample application launched on the local host with docker.

You can specify throughput per second per user with `constant_throughput`.

```
    wait_time = constant_throughput(1)
```

You can set the weight of calling a method with the `@task` annotation.

```
    @task(1)
```

For example, if constant_throughput=1, @task=1 issues 1 request per second and @task=2 issues 2 requests per second.

### Using GUI

Set environment variables in docker-compose.yml

```
    environment:
      - HOST=app
      - MODE=GUI # Specify GUI or CUI
```

After launching the docker container, access `http://localhost:3000`.

```
$ docker-compose up
```

![locust_gui_1](/images/locust_gui_1.png)

![locust_gui_2](/images/locust_gui_2.png)

- `Statistics`: Confirmation of request issuance status, response, and 90%ile value
- `Charts`: Diagram of number of requests, response time and number of users
- `Failures`: About failed requests
- `Exception`: About the situation when you catch some exception
- `Current ratio`: Scenario execution status
- `Download Data`: Download CSV of various results

example chart tab.

![locust_gui_2](/images/charts.png)

### Using CUI

Set environment variables in docker-compose.yml.

```
    environment:
      - HOST=app
      - MODE=CUI # Specify GUI or CUI
```

After launching the docker container, check that the result is output to the locust directory

```
$ docker-compose up
```

![locust_cui](/images/locust_cui.png)

![result_files](/images/result_files.png)


## Locust options

Learn about common locust options.

```
--headless: Disable the web interface, and start the test immediately. Use -u and -t to control user count and run time. Environment variable is "LOCUST_LOCUSTFILE".
--users, -u: Peak number of concurrent Locust users. Primarily used together with –headless or –autostart. Can be changed during a test by keyboard inputs w, W (spawn 1, 10 users) and s, S (stop 1, 10 users). Environment variable is "LOCUST_USERS".
--web-host: Host to bind the web interface to. Defaults to ‘*’ (all interfaces). Environment variable is "LOCUST_WEB_HOST".
--web-port, -P: Port on which to run web host. Environment variable is "LOCUST_WEB_PORT".
--spawn-rate, -r: Rate to spawn users at (users per second). Primarily used together with –headless or –autostart. Environment variable is "LOCUST_SPAWN_RATE".
--csv CSV_PREFIX: Store current request stats to files in CSV format. Setting this option will generate three files: [CSV_PREFIX]_stats.csv, [CSV_PREFIX]_stats_history.csv and [CSV_PREFIX]_failures.csv. Environment variable is "LOCUST_CSV".
--run-time, -t: Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.). Only used together with –headless or –autostart. Defaults to run forever. Environment variable is "LOCUST_RUN_TIME".
```
