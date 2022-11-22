load("render.star", "render")
load("time.star", "time")

def main(config):
    timezone = config.get("timezone") or "America/New_York"
    now = time.now().in_location(timezone)

    return render.Root(
        delay = 5000,
        child = render.Box(
            child = render.Animation(
                children = [
                    render.Text(
                        content = now.format("3:04 PM"),
                        font = "6x13",
                    ),
                    render.Text(
                        content = now.format("3 04 PM"),
                        font = "6x13",
                    ),
                ],
            ),
        ),
    )
time = raw_input().strip()

meridian = time[-2:]        # "AM" or "PM"
time_without_meridian = time[:-2]
hour = int(time[:2])

if meridian == "AM":
    hour = (hour+1) % 12 - 1
    print ("%02d" % hour) + time_without_meridian[2:]
elif meridian == "PM":
    hour += 12
    print str(hour) + time_without_meridian[2:]