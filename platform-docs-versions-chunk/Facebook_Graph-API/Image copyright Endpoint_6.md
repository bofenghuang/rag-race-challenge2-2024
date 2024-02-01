platform: Facebook
topic: Graph-API
subtopic: Image copyright Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Image copyright Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/image-copyright/


### Parameters

| Parameter | Description |
| --- | --- |
| `artist`<br><br>string | Artist/Photographer related to the copyright |
| `attribution_link`<br><br>string | The link to the rights holder where viewer can license the images. |
| `creator`<br><br>string | For agencies |
| `custom_id`<br><br>string | Any ID used internally by the copyright holder |
| `description`<br><br>string | Description of the copyrighted image |
| `filename`<br><br>string | Filename of the copyrighted image<br><br>Required |
| `geo_ownership`<br><br>list<enum {AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TP, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM, ZW}> | In which territories the copyright on the image is held<br><br>Required |
| `original_content_creation_date`<br><br>int64 | When the copyrighted image was created |
| `reference_photo`<br><br>numeric string or integer | ID of the uploaded image to be protected. This must be an unpublished, temporary photo. Please refer to the [photo documentation](https://developers.facebook.com/docs/graph-api/reference/page/photos) on how to create unpublished, temporary photos.<br><br>Required |
| `title`<br><br>string | Title of the copyrighted image |