# Members of Congress social media handles, 119th Congress

Official Instagram and X accounts for every sitting member of the 119th Congress, built for the American College of Nurse-Midwives' August recess midwifery campaign so that members and chapters could tag their own representatives correctly. Compiled and verified July 21, 2026.

Alongside it, a cosponsor table for the thirteen maternal health and midwifery bills ACNM was tracking, pulled from congress.gov.

## Files

| File | Rows | What |
|---|---|---|
| `data/house_instagram.csv` | 437 | House members (including the five delegates and the Resident Commissioner of Puerto Rico) with Instagram handle, profile link, and notes |
| `data/house_x.csv` | 437 | The same members on X |
| `data/senate_instagram.csv` | 100 | Senators on Instagram |
| `data/senate_x.csv` | 100 | Senators on X |
| `data/midwifery_bills.csv` | 13 | The tracked bills: sponsor, introduction date, committees, cosponsor count |
| `data/midwifery_bill_cosponsors.csv` | 302 | One row per cosponsor per bill, with party, state, district, date, and whether they were an original cosponsor |
| `check_links.py` | | Confirms every profile link still resolves |

Vacant seats at the time of compilation (FL-20, TX-23, and other districts left open by 2026 resignations) are excluded.

## How the handles were verified

Handles are the official congressional office account wherever one exists. Where a member keeps only a campaign or personal account, that account is listed and the Notes column says so. "None found" means no account on that platform could be identified.

Sources: each member's house.gov or senate.gov site, the House Press Gallery's official X handle list for the 119th Congress (all 437 House X handles cross-checked against it), direct checks of every Senate office site, and direct confirmation of each Instagram and X profile. X handles keep the platform's capitalization. Instagram handles are lowercase because Instagram is case-insensitive.

For campaign materials, a tag works with the handle exactly as shown, including the @.

## The bills

Nine 119th Congress bills and four from the 118th, for comparison of cosponsor growth across sessions:

- Midwives for MOMS Act (S.1599, H.R.6394, and the 118th Congress versions S.1851 and H.R.3768)
- MIDWIVES for Service Members Act (H.R.3202)
- BABIES Act (S.1598)
- Tech to Save Moms Act (S.958)
- HEALTH for MOM Act (H.R.3365)
- Rural Obstetrics Readiness Act (S.380)
- Supporting Healthy Moms and Babies Act (H.R.3762, S.1834)
- Black Maternal Health Momnibus (118th Congress H.R.3305 and S.1606)

Cosponsor lists were scraped from congress.gov in April 2026 and reflect that date. An asterisk on congress.gov marks an original cosponsor; that is the `original_cosponsor` column here.

## Keeping it current

Members resign, seats get filled, and offices rename accounts. `python check_links.py` requests every profile link and reports the ones that no longer resolve, which is usually the first sign a handle has changed. It needs only the `requests` library and takes a few minutes because it is deliberately slow (one request a second).

## License

Data: CC0. These are public officials' public accounts and public legislative records. The notes and the compilation are released without restriction. Code: MIT.
