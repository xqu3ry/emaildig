
***emaildig*** - email information digging tool. Get info from leaks, reputation, history and etc.

Tool can be useful without any API keys, but for greater efficiency you can enter your own API keys for different services

**Download emaildig:**

```
git clone https://github.com/xqu3ry/emaildig
```

```
cd emaildig
```

**Usage:**

```
python3 emaildig.py -T example@example.com
```

Or

```
python emaildig.py -T example@example.com
```

Edit your config in '*config.ini*' file

Provide your API keys to '*modules/api_keys.py*' file

Edit the entries limit you want to see for each service in '*modules/limits.py*' file

**Available  Services:**


| Hunter              | https://hunter.io/                    | 🔑     |
| ------------------- | ------------------------------------- | ------ |
| **Emailrep**        | https://emailrep.io/                  | 🔑     |
| **IpQualityScore**  | https://www.ipqualityscore.com/       | 🔑     |
| **ProxyNova**       | https://www.proxynova.com/tools/comb/ | 🚧     |
| **DeHashed**        | https://dehashed.com/                 | 🔑     |
| **LeakLookup**      | https://leak-lookup.com/              | 🔑     |
| **Leakcheck**       | https://leakcheck.io/                 | ✅ - 🔑 |
| **Snusbase**        | https://snusbase.com                  | 🔑     |
| **DataBreach**      | https://databreach.com/               | 🔑     |
| **HIBP**            | https://haveibeenpwned.com/           | 🔑     |
| **BreachDirectory** | https://breachdirectory.org           | ✅      |


