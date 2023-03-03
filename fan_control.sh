#! /bin/sh

case "$1" in
  start)
    echo "Starting fan_control.py"
    /usr/local/bin/fan_control.py &
    ;;
  stop)
    echo "Stopping fan_control.py"
    pkill -f /usr/local/bin/fan_control.py
    ;;
  *)
    echo "Usage: /etc/init.d/fan_control.sh {start|stop}"
    exit 1
    ;;
esac

exit 0