# Sprint_4
QA Python sprint 4 final task. Here we automate basic tests scenarious for https://qa-scooter.praktikum-services.ru/


Project structure:

-> locators			- locators folder. Locators for each web page are stored separately in corresponding files

-> pages			- POM files folder. Each POM is stored separately in corresponding file

-> test_data		- tests data folder. Here data for parametrized tests is stored

-> tests			- tests folder. Tests for each web page are stored separately in corresponding files

-> allure_results	- Allure reports files folder.

-> conftest.py		- fixtures

-> urls.py			- urls used in project


Project dependencies:

1. To download all necessary Python dependencies, use requirements.txt:
pip install -r requirements.txt

2. Allure. Project uses Allure to generate tests reports. Allure version is 2.22.0.
To run test with Allure report generation run: allure serve allure_results

3. Java version installed with Allure is:
openjdk 11.0.19 2023-04-18 LTS
OpenJDK Runtime Environment Corretto-11.0.19.7.1 (build 11.0.19+7-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.19.7.1 (build 11.0.19+7-LTS, mixed mode)
