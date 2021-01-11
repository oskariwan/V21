### Verkefni 1.1 HTTP staðallinn (5%)

Svaraðu spurningunum eftir bestu getu og vistaðu skjalið aftur í VEF2VF geymslu þína á Github.

---

1. Hvað er það kallað þegar vafri (client) sendir fyrirspurn um að birta ákveðna vefsíðu á vefþjón (web server)?
    1. Query
    2. Request
    3. Response
  
    **Svar:  request**  
1. Gefum okkur að vafri sendi fyrirspurn á vefþjón og vefþjónn sendir til baka boð sem segir að allt hafi heppnast án villu.  Hvaða status code fær vafrinn frá vefþjóninum?
    1. 100 OK
    2. 200 OK
    3. 404 OK
    
    **Svar:200**  
1. Hver er nýjast útgáfa HTTP staðalsins?
    1. HTTP/1.0
    2. HTTP/1.1
    3. HTTP/2.0
    
    **Svar:2.0**  
1. Hvað er sjálfgefið port á vöfrum?
    1. 80
    2. 82
    3. 88
    
    **Svar:80**  
1. Hvað er algengasta skráarsnið vefsíðna á Internetinu?
    1. .mpeg
    2. .docs
    3. .html
    
    **Svar:html**  
1. Hvert af eftirtöldu lýsir best tilgangi og hlutverki HTTP staðalsins?
    1. HTTP staðalinn er notaður til meðhöndla samskipti póstþjóna (mail servers)
    2. HTTP staðalinn er samskiptastaðall sem höndlar samskipti milli vafra (client) og vefþjóna (webservers)
    3. HTTP staðalinn er neðsta lagið í 7 laga OSI staðlinum.
    svar = 2
1. Skiptu upp eftrifarandi vefslóð (URL) http://www.mbl.is/frettir?a=2&b=3
    1. protocol: (http)
    2. host: (www.mbl.is)
    3. path: (frettir)
    4. query (?a=&b=3)
1. Hvað er átt við með því þegar talað er um að HTTP staðallinn sé stateless protocol?
    
    **Svar:protocol hvar serverinn geymir engin gögn frá notandan**  
1. Hvaða skýring passar við "GET Request" _Takið út röngu skýringuna_
    * **GET** sendir gögn á miðlara, krafan er ekki geymd í vinnsluminni og birtist ekki í vefslóð
    *svar: **GET** sækir gögn sem beðið er um af miðlara, krafan birtist í vefslóðinni og er geymd í vinnsluminni vafrans
1. Hvaða skýring passar við POST request?
    * **POST** sendir gögn á miðlara, krafan birtist ekki í vefslóð og fer ekki í vinnsluminnið (Cache)
    * **POST** sækir gögn sem beðið er um af miðlara, krafan birtist í vefslóðinni og er geymd í vinnsluminni vafrans


