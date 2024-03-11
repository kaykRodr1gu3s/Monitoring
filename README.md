# Monitoring

Monitoring is a repository that monitoring the sites: [Cert.br](https://stats.cert.br/), [cveDetails](https://www.cvedetails.com/cisa-known-exploited-vulnerabilities/kev-1.html?&order=1&trc=988&sha=7cc3a9bfde72b01401aa6778d4ddc1b96eb2776d) and [paste.fo](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/paste.fo](https://paste.fo/recent)), using web scrapping technique.

---

## index
1 - [Requirements](#Requirements)

2- [How to use](#How-to-use)

3 - [Saved files](#Saved-files)

4 - [How to contribute](#How-to-contribute)

## Requirements
 It will be necessary to install some python libraries, they're : bs4, requests and PyYaml.


 Use the code below to install the libraries.

 ```bash
pip install bs4
pip install requests
pip install PyYaml
```


---

## How to use

To start monitoring execute the code, choice one of the option:  

* [Cert.br](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/certBR)

* [cveDetails](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cveDetails)

* [paste.fo](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/paste.fo)


All the monitoring will show the result as output in the terminal or will save the result in .csv or .yml file.



---

### Saved files

On [Cert.br](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cert.br) monitoring, the datas extracted will be saved in a .csv [example](https://github.com/kaykRodr1gu3s/Monitoring/blob/main/certBR/Honeypots/tcp-udp/udp_ports.csv).

On [cveDetails](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/cveDetails) monitoring, the datas extracted will be saved in a .yaml and .csv files [example of a .csv](https://github.com/kaykRodr1gu3s/Monitoring/blob/main/cveDetails/Csv%20datas/cvedetails.csv), [example of a .yaml]

On [paste.fo](https://github.com/kaykRodr1gu3s/Monitoring/tree/main/paste.fo) monitoring, all the datas extrated, will be printed on the terminal as output.


---

## How to contribute 

 1. Fork the repository.
 2. Create a branch for your contribution: `git checkout -b feature-nova`.
 3. Make the desired changes and commit: `git commit -m "Add new functionality"`.
 4. Push to your branch: `git push origin new-feature`.
 5. Open a pull request.

## Contact

- Linkedin: [Kayk Rodrigues](https://www.linkedin.com/in/kayk-rodrigues-504a03273)
- Telegram: [Kayk Rodrigues](https://t.me/kaykRodrigues)
