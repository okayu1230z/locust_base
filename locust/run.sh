#!/bin/sh

if [ $MODE = "GUI" ]; then
    echo “start locust testing by GUI”
    locust --web-port 3000
else
    echo “start locust testing by CUI”
    locust --headless --web-port 3000 --csv result
fi

# locust optioons
#--headless: Disable the web interface, and start the test immediately. Use -u and -t to control user count and run time. Environment variable is "LOCUST_LOCUSTFILE".
#--users, -u: Peak number of concurrent Locust users. Primarily used together with –headless or –autostart. Can be changed during a test by keyboard inputs w, W (spawn 1, 10 users) and s, S (stop 1, 10 users). Environment variable is "LOCUST_USERS".
#--web-host: Host to bind the web interface to. Defaults to ‘*’ (all interfaces). Environment variable is "LOCUST_WEB_HOST".
#--web-port, -P: Port on which to run web host. Environment variable is "LOCUST_WEB_PORT".
#--spawn-rate, -r: Rate to spawn users at (users per second). Primarily used together with –headless or –autostart. Environment variable is "LOCUST_SPAWN_RATE".
#--csv CSV_PREFIX: Store current request stats to files in CSV format. Setting this option will generate three files: [CSV_PREFIX]_stats.csv, [CSV_PREFIX]_stats_history.csv and [CSV_PREFIX]_failures.csv. Environment variable is "LOCUST_CSV".
#--run-time, -t: Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.). Only used together with –headless or –autostart. Defaults to run forever. Environment variable is "LOCUST_RUN_TIME".