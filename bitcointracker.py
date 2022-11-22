load("render.star", "render")
load("http.star", "http")
load("encoding/base64.star", "base64")

COINDESK_PRICE_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Load Bitcoin icon from base64 encoded data
BTC_ICON = base64.decode("""
iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAlklEQVQ4T2NkwAH+H2T/jy7FaP+
TEZtyDEG4Zi0TTPXXzoDF0A1DMQRsADbN6MZdO4NiENwQbAbERh1lWLzMmgFGo5iFZBDYEFwuwG
sISCPUIKyGgDRjAyBXYXMNIz5XgDQga8TpLboYgux8DO/AwoUuLiEqTLBFMcmxQ7V0gssgklIsL
AYozjsoBoE45OZi5DRBSnkCAMLhlPBiQGHlAAAAAElFTkSuQmCC
""")

def main():
    rep = http.get(COINDESK_PRICE_URL)
    if rep.status_code != 200:
        fail("CoinDesk request failed with status %d", rep.status_code)

    rate = rep.json()["bpi"]["USD"]["rate_float"]

    return render.Root(
        child = render.Row( # Row lays out its children horizontally
                children = [
                    render.Image(src=BTC_ICON),
                    render.Text("$%d" % rate),
                ],
        )
    )
