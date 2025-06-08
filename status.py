import os
import datetime
import platform
import subprocess

import pytz

START_TIME_TIMESTAMP_UTC = int(
    datetime.datetime.timestamp(datetime.datetime.now(pytz.UTC))
)
PLATFORM = f"{platform.uname()[1]} ({platform.uname()[2]})"


def exec_cmd(command):
    try:
        return str(
            subprocess.check_output(
                command, shell=True, text=True, stderr=subprocess.DEVNULL
            ).strip()
        )

    except Exception as exc:
        return exc.__class__.__name__


def get_uptime():
    seconds = (
        int(datetime.datetime.timestamp(datetime.datetime.now(pytz.UTC)))
        - START_TIME_TIMESTAMP_UTC
    )

    intervals = (("week", 604800), ("day", 86400), ("hour", 3600), ("minute", 60))
    result = []

    if seconds < 60:
        result.append(f"{seconds} seconds")

    else:
        for time_type, count in intervals:
            value = seconds // count

            if value:
                seconds -= value * count
                result.append(f"{value} {time_type if value == 1 else time_type + 's'}")

    if len(result) > 1:
        result[-1] = "and " + result[-1]

    return ", ".join(result)


def get_uptime_since(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, pytz.UTC).strftime(
        "%A, %B %d %Y, %I:%M:%S %p"
    )


def get_status(service_name):
    systemd_status = exec_cmd(f"systemctl status {service_name}")

    try:
        systemd_status = systemd_status.strip().split("\n")[2].strip()

    except IndexError:
        pass

    commit_hash = exec_cmd("git log -1 --pretty=format:%h")
    commit_message = exec_cmd(f"git log -1 --pretty=format:%s {commit_hash}")

    data = {
        "status": {
            "git": {"commit_hash": commit_hash, "commit_message": commit_message},
            "uptime": {
                "uptime": get_uptime(),
                "since": get_uptime_since(START_TIME_TIMESTAMP_UTC),
            },
            "systemd_status": systemd_status,
            "website_mode": os.getenv("WEBSITE_MODE"),
            "platform": PLATFORM,
        }
    }

    return data
