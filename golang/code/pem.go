// 测试证书，无需理会
package main

// import (
// 	"encoding/pem"
// )
import "fmt"

// import "os"

func main() {
	var key = `-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDhgXqUH/r/5Y+T
5dHeitbomhhvGa30XIDhjYXfupeutUaec3nihKzgJY8Ufoj0Y7OutSz9RbbmYSr7
6iIniJxJrdSO5v4vUG+Vd68K7mmYzZsRxGKguA4TC2B3rQ1lPqygo+YNCkAzQTJe
P4PHzm6KNhZdK5ijgME+2c98N9ole+GNj+FpctHbfSn7CcXj8MQw4FJM2jaiMmR/
vfC0pe65dt9PYv3V7MbIxWyk9hgSCwrAjxtbEoYtt4JzldOiNDXTiA1UxJjqQvEM
hTQ+8JZVOdaiBdh4a7NeExcjOTSihICLd8cdaNE0sX26ZMBNStbcGODFZas+TgRy
rAyJlylPAgMBAAECggEBAMdvI2FtBybZdyltzzXpxDbiUUmwhE/gn3rbFtLOyucQ
Gux3ZAwZGmsBzJBrd+PraTXRtYAo76C/vqwcXShpgQ8IVTwsvhBKKuUdfAlG4Mzq
yYHlFPTe0lO1dBNjUL2BuFo5mXNe5Xhu6ITB12IWB1zkiNLNg6jWbhGPwBgzrRIH
3EJr7d3ncdpQLjgtKcsSUbFy++a18QxCyaVopzpXkpLhkuP9JGSm1YhJdax+TpPN
ES9z7hwR/EGQlt2xZI15nHt9vGOFZdUocIUbEy9yYZTE4RK3MJW51HQG2JDow9XK
6u/xdW+1thNIW3a/T8Psv9JLceYg0SfWLH4W0D3Je0ECgYEA9yPlet0chqjJN7BF
2Ifd7m2uOMqW2ZoDX4Nzy5S6qrvYP0gpzXNUo/yGZJYqOGWDGWbk+r66ZtFNmjEG
6MGRO/keEK5m7ImF2BE25/URufqqdPbFqHzghn1e9zThnkcDTC1mJQT9HlBUejRQ
/oOBQRaQhbFdrmhhSt7WwsUHyEMCgYEA6ZcI2VezQqy0Z0ihXHNybgDMfRwjPsaV
41iS4PNnDoS4pCxTH3y6S4HfAC/sOg0Dl52OJy7Xbpnf7F3M2W1Y+fjT0J4E3wld
EW5N8YCmbTrWGIcjMsmj73CtkUkuivNg+eA4+OhaAYHkdQ7hhIDoRjzF2uCATjVm
7bZyUq/qwAUCgYAM9f/58pCla0KqPf9bvLxh3bSuW8mPfelBYBZ5jcJAY/uSTgmL
Mco1k2/E5K8wJ/q5IVFO6SPDcqScOof/Ou+P8p+mBk91hjzTuQtlHNAiLcg0vCBf
lrT7uKV7V3WhpF3C5/qcZGeV6GaVxhqdTm4/6JwJtuSP2f+IOqmOq2CeGwKBgHyV
q4iQN/HVvxpfKIDwqhV1o5sOyNWQgR0SfrQv3cVmkDwvz925XnsrN08YQDvt+P6C
b/ECELDSrRWaKcnFgnFAf2iC/0Id8l97n2KxJRKZENtgKCvMU/0+8bPNfl9p000y
g/BtrKOlLb4pQ6qyPjBH9Zb5qjUMUmtypaLoZKIpAoGAPyBRL7sdGmwcGBQ8TcFw
Kf3dVGqHNZZQOydSSn0I3TSiTTIO1ODZJiGMBBch/UFdDa11Pbstk0b+dePQAqbX
qVj3f4doyPe+/Rk1DJHlEiCuWyMGDHWecnzaNX3cRxvPQ5Vx21CiWjRiD9G3itWN
KYiB+KYDS5BuNmuUduNsrbA=
-----END PRIVATE KEY-----`
	fmt.Printf("%q", key)
	var pubkey = `-----BEGIN CERTIFICATE-----
MIIFVjCCBD6gAwIBAgISAyCTlNGvYzXX3/N1M5FuJjBCMA0GCSqGSIb3DQEBCwUA
MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD
ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0yMDA4MTcwMTU2MzFaFw0y
MDExMTUwMTU2MzFaMBoxGDAWBgNVBAMMDyouY3NmdGdyb3VwLmNvbTCCASIwDQYJ
KoZIhvcNAQEBBQADggEPADCCAQoCggEBAOGBepQf+v/lj5Pl0d6K1uiaGG8ZrfRc
gOGNhd+6l661Rp5zeeKErOAljxR+iPRjs661LP1FtuZhKvvqIieInEmt1I7m/i9Q
b5V3rwruaZjNmxHEYqC4DhMLYHetDWU+rKCj5g0KQDNBMl4/g8fOboo2Fl0rmKOA
wT7Zz3w32iV74Y2P4Wly0dt9KfsJxePwxDDgUkzaNqIyZH+98LSl7rl2309i/dXs
xsjFbKT2GBILCsCPG1sShi23gnOV06I0NdOIDVTEmOpC8QyFND7wllU51qIF2Hhr
s14TFyM5NKKEgIt3xx1o0TSxfbpkwE1K1twY4MVlqz5OBHKsDImXKU8CAwEAAaOC
AmQwggJgMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYB
BQUHAwIwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUamVop913BNthKeF9XdSvxKXZ
UMowHwYDVR0jBBgwFoAUqEpqYwR93brm0Tm3pkVl7/Oo7KEwbwYIKwYBBQUHAQEE
YzBhMC4GCCsGAQUFBzABhiJodHRwOi8vb2NzcC5pbnQteDMubGV0c2VuY3J5cHQu
b3JnMC8GCCsGAQUFBzAChiNodHRwOi8vY2VydC5pbnQteDMubGV0c2VuY3J5cHQu
b3JnLzAaBgNVHREEEzARgg8qLmNzZnRncm91cC5jb20wTAYDVR0gBEUwQzAIBgZn
gQwBAgEwNwYLKwYBBAGC3xMBAQEwKDAmBggrBgEFBQcCARYaaHR0cDovL2Nwcy5s
ZXRzZW5jcnlwdC5vcmcwggEEBgorBgEEAdZ5AgQCBIH1BIHyAPAAdQBep3P531bA
57U2SH3QSeAyepGaDIShEhKEGHWWgXFFWAAAAXP6WNKeAAAEAwBGMEQCIFKqAHO9
2RExNqeiP6Cnq+trGl2U5EtQzxZiGMnuHjmXAiAKaHq+ZNbWMgIzvxt0yw2gqj07
3le6NJLAfDCO0ZLWKAB3ALIeBcyLos2KIE6HZvkruYolIGdr2vpw57JJUy3vi5Be
AAABc/pY0pAAAAQDAEgwRgIhANHsekO3zc1EU0rywUEy+CNzOpFRn+ooBwJAohwQ
4emaAiEAyhbDN0I5KwQq1OQhM+8/twtaLtuA4SnMJEPDm/QEXSEwDQYJKoZIhvcN
AQELBQADggEBAHFrhyCda8knA0Z47upDbZwdS+dH+RB9KrDVUywMJyGF5s4bSmys
TbMlPGmlT/5QkQ6Tht9+KgCDAKA5bETq45cYU5nNlAvK26CxfAhyNOR4lq8TmqLi
jQPbFZFXgthsirAziUwAsCxhsLPS8AqhDH/4J28pLY73vp6qI4/fcuRZlY1OYiSl
uBuXViO7Mlnzqe9wzKMzx/IkgCQQ+AgHd2b3fS29F81JVpX0zPCzWywLBN5cDnwm
ERaJCTGpmggqBVrrWT5cv5cnBYRA7MY/7477HdWd13Pr41lJKIPCX3MMj/L2OYxw
JCFP+qU3SoF/Q3I+gtNWuJQFxfzQyBD6OpQ=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/
MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
DkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0Nlow
SjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMT
GkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EF
q6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8
SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0
Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWA
a6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj
/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0T
AQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIG
CCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNv
bTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9k
c3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAw
VAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcC
ARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAz
MDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwu
Y3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsF
AAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJo
uM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/
wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwu
X4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlG
PfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6
KOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==
-----END CERTIFICATE-----`
	println("\n")
	fmt.Printf("%q", pubkey)
	// a, b := pem.Decode(publicKey)
	// println(a)
	// println(b)
}
