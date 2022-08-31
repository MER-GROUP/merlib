<div id="top"></div>
<!-- Best-README-Template ---------------------------------------------------------------------->
<!--
*** https://github.com/othneildrew/Best-README-Template
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->
<!-- ------------------------------------------------------------------------------------------->

<!-- PROJECT SHIELDS --------------------------------------------------------------------------->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!--
[![LinkedIn][linkedin-shield]][linkedin-url]
-->
<!-- ------------------------------------------------------------------------------------------->

<!-- PROJECT LOGO ------------------------------------------------------------------------------>
<div align="center">
  <!--
  <a href="https://github.com/MER-GROUP/merlib">
    <img src="ico/merlib.png" alt="Logo" width="280" height="280">
  </a>
  -->

  <h1 align="center"><b>merlib</b></h1>

  <p align="center">
        <h2><b>merlib is modules and classes in Python/Cython/C for everyday work</b><br />
            <i>[merlib - это модули и классы на Python/Cython/C для повседневной работы]</i></h2>
        <a href="https://github.com/MER-GROUP/merlib">View [Просмотр]</a>
        ·
        <a href="https://github.com/MER-GROUP/merlib/issues">Report Bug [Сообщить об ошибке]</a>
        ·
        <a href="https://github.com/MER-GROUP/merlib/issues">Request Feature [Внести изменение]</a>
  </p>
</div>
<!-- ------------------------------------------------------------------------------------------->

<!-- TABLE OF CONTENTS ------------------------------------------------------------------------->
<details>
  <summary>Table of Contents [Содержание]</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project [Об этом проекте]</a>
      <ul>
        <li><a href="#built-with">Built With [Инструменты разработки]</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started [Начало работы]</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites [Подготовка к установке]</a></li>
        <li><a href="#installation">Installation [Установка]</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage [Использование]</a></li>
    <li><a href="#roadmap">Roadmap [История изменений]</a></li>
    <li><a href="#contributing">Contributing [Вклад в проект]</a></li>
    <li><a href="#license">License [Лицензия]</a></li>
    <li><a href="#contact">Contact [Контакты]</a></li>
    <li><a href="#acknowledgments">Acknowledgments [Используемын ресурсы]</a></li>
  </ol>
</details>
<!-- ------------------------------------------------------------------------------------------->

<!-- ABOUT THE PROJECT ------------------------------------------------------------------------->
## **About The Project [Об этом проекте]**
<!-- 
[![Product Name Screen Shot][product-screenshot]](https://example.com) 
-->
**merlib is modules and classes in Python/Cython/C for everyday work.**

[*merlib - это модули и классы на Python/Cython/C для повседневной работы.*]

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- Built With -------------------------------------------------------------------------------->
### **Built With [Инструменты разработки]**

<!-- 
This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
[В этом разделе должны быть перечислены все основные фреймворки / библиотеки, используемые для начальной загрузки вашего проекта. Оставьте любые дополнения/плагины для раздела "Подтверждения". Вот несколько примеров.] 
-->

<!-- 
* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] 
-->

* [![Python][Python.org]][Python-url]
* [![Kivy][Kivy.org]][Kivy-url]
* [![Plyer][Plyer.org]][Plyer-url]
* [![Pyjnius][Pyjnius.org]][Pyjnius-url]
* [![Debian][Debian.org]][Debian-url]
* [![VSCode][VSCode.org]][VSCode-url]
* [![Git][Git.org]][Git-url]

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- GETTING STARTED --------------------------------------------------------------------------->
## **Getting Started [Начало работы]**

**To install and run this program, follow the steps described below.**

[*Для установки и запуска данной программы проделайте шаги описанные ниже.*]

### **Prerequisites [Подготовка к установке]**

1. Clone the repo [*Скопируйте репозиторий*]:
  ```sh
  git clone https://github.com/MER-GROUP/merlib.git
  ```
2. Copy it into your project and use it as regular classes [*Скопируйте в ваш проект и используйте как обычные классы*]

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- USAGE EXAMPLES ---------------------------------------------------------------------------->
## **Usage [Использование]**

1. Example of exporting a method from a class [*Пример вывоза метода из класса*]:
   ```sh
   from merlib.fs.File import File 
   file = File()
   file.file_create('./test.txt', __file__)
   file.file_create('test.txt', __file__)
   ```

2. The classes are documented in detail [*Классы подробно задокументированы*]:
   ```sh
   from merlib.fs.File import File 
   file = File()
   print(file.file_create.__doc__)
   ```

3. The name of the class corresponds to its implementation [*Наименование класса соответствует его реализации*]

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- ROADMAP ----------------------------------------------------------------------------------->
## **Roadmap [История изменений]**

- [x] merlib.android.API [*работа с API ОС Android*]
- [x] merlib.cython.alg.BogoSort.BogoSort [*алгоритм болотной сортировки*]
- [x] merlib.cython.alg.MonteCarlo.MonteCarlo [*алгоритм Монте Карло*]
- [x] merlib.cython.example.cython_test_factorial [*пример написания алгоритма на Cython*]
- [x] merlib.fs.File [*работа с файлами*]
- [x] merlib.kivy.Design [*работа с объектами фреймворка kivy*]
- [x] merlib.net.MacAddress [*получение мак адреса устройства*]
- [x] merlib.sys.OsName [*получение имени ОС*]
- [x] merlib.sys.OsUniqueNum [*получение уникального номера устройства*]
- [x] merlib.sys.Translate [*работа с локализацией*]
- [ ] Multi-language Support [*Поддержка нескольких языков*]
    - [ ] English
    - [ ] Русский

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- CONTRIBUTING ------------------------------------------------------------------------------>
## **Contributing [Вклад в проект]**

**Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are __greatly appreciated__.**

[*Вклад - это то, что делает сообщество с открытым исходным кодом таким удивительным местом для обучения, вдохновения и творчества. Любой ваш вклад __очень ценится__.*]

**If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!**

[*Если у вас есть предложение, которое сделало бы проект лучше, пожалуйста, сделайте форк репозитория, внесите изменение и создайте запрос на рассмотрение вашего изменения. Вы также можете просто открыть проблему с тегом "улучшение".
Не забудьте дать проекту звезду! Еще раз спасибо!*]

1. Fork the Project [*Сделайте форк проекта*]
2. Create your Feature Branch [*Создайте свою ветку*]:
   ```sh
   git checkout -b feature/merlib
   ```
3. Commit your Changes [*Внесите изменения*]:
   ```sh
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the Branch [*Отправте на рассмотрение ваши изменения*]:
   ```sh
   git push origin feature/AmazingFeature`
   ```
5. Open a Pull Request [*Откройке ваш запрос*]

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- LICENSE ----------------------------------------------------------------------------------->
## **License [Лицензия]**

**Distributed under the MIT License. See `LICENSE` for more information.**

[*Распространяется по лицензии MIT. Дополнительные сведения см. в разделе `ЛИЦЕНЗИЯ`.*]

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- CONTACT ----------------------------------------------------------------------------------->
## **Contact [Контакты]**

Max Ramanenka (Red Alert)  - i@mer-group.ru

Project Link [*Ссылка на проект*]: [https://github.com/MER-GROUP/merlib](https://github.com/MER-GROUP/merlib)

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- ACKNOWLEDGMENTS --------------------------------------------------------------------------->
## **Acknowledgments [Используемын ресурсы]**

* [Python](https://www.python.org/)
* [Kivy](https://kivy.org/#home)
* [Plyer](https://github.com/kivy/plyer)
* [Pyjnius](https://github.com/kivy/pyjnius)
* [Buildozer](https://github.com/kivy/buildozer)
* [Json](https://www.json.org/json-en.html)
* [Debian](https://www.debian.org/)
* [VSCode](https://code.visualstudio.com/)
* [Git](https://git-scm.com/)
* [Markdown](https://www.markdownguide.org/)

<p align="right">(<a href="#top">back to top [вернуться к началу]</a>)</p>
<!-- ------------------------------------------------------------------------------------------->

<!-- MARKDOWN LINKS & IMAGES ------------------------------------------------------------------->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- contributors -->
[contributors-shield]: https://img.shields.io/github/contributors/MER-GROUP/merlib.svg?style=for-the-badge
[contributors-url]: https://github.com/MER-GROUP/merlib/graphs/contributors

<!-- forks -->
[forks-shield]: https://img.shields.io/github/forks/MER-GROUP/merlib.svg?style=for-the-badge
[forks-url]: https://github.com/MER-GROUP/merlib/network/members

<!-- stars -->
[stars-shield]: https://img.shields.io/github/stars/MER-GROUP/merlib.svg?style=for-the-badge
[stars-url]: https://github.com/MER-GROUP/merlib/stargazers

<!-- issues -->
[issues-shield]: https://img.shields.io/github/issues/MER-GROUP/merlib.svg?style=for-the-badge
[issues-url]: https://github.com/MER-GROUP/merlib/issues

<!-- license -->
[license-shield]: https://img.shields.io/github/license/MER-GROUP/merlib.svg?style=for-the-badge
[license-url]: https://github.com/MER-GROUP/merlib/blob/master/LICENSE

<!-- linkedin -->
<!--
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
-->

<!-- screenshot -->
<!-- 
[product-screenshot]: images/screenshot.png 
-->

<!-- Next -->
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/

<!-- React -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/

<!-- Vue -->
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/

<!-- Angular -->
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/

<!-- Svelte -->
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/

<!-- Laravel -->
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com

<!-- Bootstrap -->
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

<!-- JQuery -->
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

<!-- Python -->
[Python.org]: https://img.shields.io/badge/python-7279D8?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/

<!-- Kivy -->
[Kivy.org]: https://img.shields.io/badge/kivy-49444E?style=for-the-badge&logo=python&logoColor=white
[Kivy-url]: https://kivy.org/

<!-- Plyer -->
[Plyer.org]: https://img.shields.io/badge/plyer-49444E?style=for-the-badge&logo=python&logoColor=white
[Plyer-url]: https://github.com/kivy/plyer

<!-- Pyjnius -->
[Pyjnius.org]: https://img.shields.io/badge/pyjnius-49444E?style=for-the-badge&logo=python&logoColor=white
[Pyjnius-url]: https://github.com/kivy/pyjnius

<!-- Buildozer -->
[Buildozer.org]: https://img.shields.io/badge/buildozer-49444E?style=for-the-badge&logo=python&logoColor=white
[Buildozer-url]: https://github.com/kivy/buildozer

<!-- Json -->
[Json.org]: https://img.shields.io/badge/json-D0B4C4?style=for-the-badge&logo=json&logoColor=white
[Json-url]: https://json.org/

<!-- Debian -->
[Debian.org]: https://img.shields.io/badge/debian-81476C?style=for-the-badge&logo=debian&logoColor=white
[Debian-url]: https://debian.org/

<!-- VSCode -->
[VSCode.org]: https://img.shields.io/badge/vscode-3E7384?style=for-the-badge&logo=visualstudio&logoColor=white
[VSCode-url]: https://code.visualstudio.com/

<!-- Git -->
[Git.org]: https://img.shields.io/badge/git-F92929?style=for-the-badge&logo=git&logoColor=white
[Git-url]: https://git-scm.com/
<!-- ------------------------------------------------------------------------------------------->