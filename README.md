# MLIT NOx / CO2 Lookup  (Vercel ready)

Search a model code (MXPH10 / 6AA-MXPH10) -> original MLIT CO2 sheet (Excel + PDF) and the original NOx page (PDF).

## Deploy on Vercel
1. Put this folder in a GitHub repo (or use the Vercel CLI):  `npm i -g vercel`  then  `vercel --prod`  inside this folder.
2. Framework preset: **Other**. No build command. (vercel.json is already set up.)
3. Done. `public/` is the website, `api/*.py` are the download functions, `_data/` holds the MLIT data.

Deployment size is about 48 MB (tools/ is excluded by .vercelignore).

## Run locally
    pip install -r requirements.txt
    python dev_server.py        ->  http://localhost:8000

## Add / update MLIT data
Put new .xlsx in `tools/sources/co2` (old .xls: save as .xlsx first) or new .pdf in `tools/sources/nox`, then:
    pip install -r requirements.txt pdfplumber pypdfium2
    python tools/build_static.py --reindex
and deploy again.

## Notes
- CO2 PDF is drawn from the MLIT sheet layout (same columns, merges, borders, header) with IPAex Gothic font.
- NOx PDF is the untouched original page from the MLIT PDF.
- Not indexed (text unreadable): MAZDA NOX (1).pdf, MERCEDES-BENZ NOX (2).pdf, PORSCHE NOX.pdf
