# Monitoring

Monitoring é um repositório, que visa monitorar diversos sites: cert.br, past.fo e cveDetails.com. utilizando técnicas de Web-scrapping


---

## Pré- requisitos
 será necessário algumas bibliotecas python: bs4, requests PyYaml

 ```bash
pip install bs4
pip install requests
pip install PyYaml
```




## Como usar

É muito simples de usar, basta apenas executar o qual código de qual site você deseja monitorar.

* [Cert.br](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cert.br)

* [cveDetails](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cveDetails)

* [paste.fo](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/paste.fo)

---

### Arquivos salvos

No monitoramento do[Cert.br](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cert.br), os dados extraídos são salvos em .csv [exemplo](https://github.com/kaykRodr1gu3s/Monitoring/blob/main/cert.br/Honeypots/tcp-udp/tcp_ports.csv).

No Script do [cveDetails](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cveDetails), os dados extrídos são salvos em .yaml [exemplo de um arquivo yaml](https://github.com/kaykRodr1gu3s/Monitoring/blob/main/cveDetails/cve_files/CVE-2023-5631.yaml).

No código [paste.fo](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/paste.fo), todos os dados extraídos são mostrado em seu terminal como output.


---

## Como contribuir

Clone o repositório , efetue as suas mudanças , após isso efetue o Pull Request
