# Starter photos

`seed_site` loads these into Wagtail Images when the site is seeded. Any file
that's missing is skipped, and that spot shows its illustration or icon instead.
These are stand-ins (licensed stock, or the clinic's own photos). The clinic can
replace any of them later in the Wagtail admin.

| File | Where it shows |
|---|---|
| `slide-1.jpg` … `slide-3.jpg` | Home slider frame (cropped square) |
| `team-group.jpg` | The clinic's real team photo: home slide 4 and the top of Our Providers. Never stock. |
| `providers-standin.jpg` | Stand-in team photo Russell supplied for the top of Our Providers only, until `team-group.jpg` exists. Not used on the slider. |
| `service-pediatric-audiology.jpg` | Audiology page, beside "Your first visit" |
| `service-pediatric-occupational-therapy.jpg` | Occupational Therapy page |
| `service-pediatric-physical-therapy.jpg` | Physical Therapy page |
| `service-speech-language-therapy.jpg` | Speech-Language Therapy page |
| `visit-01-building.jpg` … `visit-09-goodbye.jpg` | First visit photo story (clinic photos only, never stock) |
| `providers/<slug>.jpg` | A provider's headshot, named like the end of their profile address (e.g. `providers/kimberly-oviedo.jpg` for /our-providers/kimberly-oviedo/). Cropped square, aimed at the upper part of a tall photo. Use 800px wide or more, and strip location data from phone photos. |

Visit story files: `visit-01-building`, `visit-02-parking`, `visit-03-door`,
`visit-04-front-desk`, `visit-05-waiting-room`, `visit-06-hallway`,
`visit-07-bathroom`, `visit-08-gym`, `visit-09-goodbye`.
