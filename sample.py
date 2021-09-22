import json


sample = """{
  "tracks" : {
    "href" : "https://api.spotify.com/v1/search?query=billie+eilish+&type=track&offset=0&limit=2",
    "items" : [ {
      "album" : {
        "album_type" : "single",
        "artists" : [ {
          "external_urls" : {
            "spotify" : "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
          },
          "href" : "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
          "id" : "6qqNVTkY8uBg9cP3Jd7DAH",
          "name" : "Billie Eilish",
          "type" : "artist",
          "uri" : "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
        }, {
          "external_urls" : {
            "spotify" : "https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny"
          },
          "href" : "https://api.spotify.com/v1/artists/6LuN9FCkKOj5PcnpouEgny",
          "id" : "6LuN9FCkKOj5PcnpouEgny",
          "name" : "Khalid",
          "type" : "artist",
          "uri" : "spotify:artist:6LuN9FCkKOj5PcnpouEgny"
        } ],
        "external_urls" : {
          "spotify" : "https://open.spotify.com/album/2sBB17RXTamvj7Ncps15AK"
        },
        "href" : "https://api.spotify.com/v1/albums/2sBB17RXTamvj7Ncps15AK",
        "id" : "2sBB17RXTamvj7Ncps15AK",
        "images" : [ {
          "height" : 640,
          "url" : "https://i.scdn.co/image/ab67616d0000b2738a3f0a3ca7929dea23cd274c",
          "width" : 640
        }, {
          "height" : 300,
          "url" : "https://i.scdn.co/image/ab67616d00001e028a3f0a3ca7929dea23cd274c",
          "width" : 300
        }, {
          "height" : 64,
          "url" : "https://i.scdn.co/image/ab67616d000048518a3f0a3ca7929dea23cd274c",
          "width" : 64
        } ],
        "name" : "lovely (with Khalid)",
        "release_date" : "2018-04-19",
        "release_date_precision" : "day",
        "total_tracks" : 1,
        "type" : "album",
        "uri" : "spotify:album:2sBB17RXTamvj7Ncps15AK"
      },
      "artists" : [ {
        "external_urls" : {
          "spotify" : "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
        },
        "href" : "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
        "id" : "6qqNVTkY8uBg9cP3Jd7DAH",
        "name" : "Billie Eilish",
        "type" : "artist",
        "uri" : "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
      }, {
        "external_urls" : {
          "spotify" : "https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny"
        },
        "href" : "https://api.spotify.com/v1/artists/6LuN9FCkKOj5PcnpouEgny",
        "id" : "6LuN9FCkKOj5PcnpouEgny",
        "name" : "Khalid",
        "type" : "artist",
        "uri" : "spotify:artist:6LuN9FCkKOj5PcnpouEgny"
      } ],
      "available_markets" : [ "AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CH", "CI", "CL", "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ES", "FI", "FJ", "FM", "FR", "GA", "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR", "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN", "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR", "ST", "SV", "SZ", "TD", "TG", "TH", "TL", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW" ],
      "disc_number" : 1,
      "duration_ms" : 200185,
      "explicit" : False,
      "external_ids" : {
        "isrc" : "USUM71804190"
      },
      "external_urls" : {
        "spotify" : "https://open.spotify.com/track/0u2P5u6lvoDfwTYjAADbn4"
      },
      "href" : "https://api.spotify.com/v1/tracks/0u2P5u6lvoDfwTYjAADbn4",
      "id" : "0u2P5u6lvoDfwTYjAADbn4",
      "is_local" : False,
      "name" : "lovely (with Khalid)",
      "popularity" : 86,
      "preview_url" : null,
      "track_number" : 1,
      "type" : "track",
      "uri" : "spotify:track:0u2P5u6lvoDfwTYjAADbn4"
    }, {
      "album" : {
        "album_type" : "album",
        "artists" : [ {
          "external_urls" : {
            "spotify" : "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
          },
          "href" : "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
          "id" : "6qqNVTkY8uBg9cP3Jd7DAH",
          "name" : "Billie Eilish",
          "type" : "artist",
          "uri" : "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
        } ],
        "available_markets" : [ "AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CH", "CI", "CL", "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ES", "FI", "FJ", "FM", "FR", "GA", "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR", "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN", "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR", "ST", "SV", "SZ", "TD", "TG", "TH", "TL", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW" ],
        "external_urls" : {
          "spotify" : "https://open.spotify.com/album/0S0KGZnfBGSIssfF54WSJh"
        },
        "href" : "https://api.spotify.com/v1/albums/0S0KGZnfBGSIssfF54WSJh",
        "id" : "0S0KGZnfBGSIssfF54WSJh",
        "images" : [ {
          "height" : 640,
          "url" : "https://i.scdn.co/image/ab67616d0000b27350a3147b4edd7701a876c6ce",
          "width" : 640
        }, {
          "height" : 300,
          "url" : "https://i.scdn.co/image/ab67616d00001e0250a3147b4edd7701a876c6ce",
          "width" : 300
        }, {
          "height" : 64,
          "url" : "https://i.scdn.co/image/ab67616d0000485150a3147b4edd7701a876c6ce",
          "width" : 64
        } ],
        "name" : "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?",
        "release_date" : "2019-03-29",
        "release_date_precision" : "day",
        "total_tracks" : 14,
        "type" : "album",
        "uri" : "spotify:album:0S0KGZnfBGSIssfF54WSJh"
      },
      "artists" : [ {
        "external_urls" : {
          "spotify" : "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
        },
        "href" : "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
        "id" : "6qqNVTkY8uBg9cP3Jd7DAH",
        "name" : "Billie Eilish",
        "type" : "artist",
        "uri" : "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
      } ],
      "available_markets" : [ "AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CH", "CI", "CL", "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ES", "FI", "FJ", "FM", "FR", "GA", "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR", "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN", "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR", "ST", "SV", "SZ", "TD", "TG", "TH", "TL", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW" ],
      "disc_number" : 1,
      "duration_ms" : 156370,
      "explicit" : False,
      "external_ids" : {
        "isrc" : "USUM71900771"
      },
      "external_urls" : {
        "spotify" : "https://open.spotify.com/track/7qEKqBCD2vE5vIBsrUitpD"
      },
      "href" : "https://api.spotify.com/v1/tracks/7qEKqBCD2vE5vIBsrUitpD",
      "id" : "7qEKqBCD2vE5vIBsrUitpD",
      "is_local" : False,
      "name" : "ilomilo",
      "popularity" : 71,
      "preview_url" : null,
      "track_number" : 11,
      "type" : "track",
      "uri" : "spotify:track:7qEKqBCD2vE5vIBsrUitpD"
    } ],
    "limit" : 2,
    "next" : "https://api.spotify.com/v1/search?query=billie+eilish+&type=track&offset=2&limit=2",
    "offset" : 0,
    "previous" : null,
    "total" : 1207
  }
}
}"""
samples = json.loads(sample)
print(samples["tracks"]["items"][0]["href"])