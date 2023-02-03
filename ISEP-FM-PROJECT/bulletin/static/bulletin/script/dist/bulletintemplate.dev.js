"use strict";

window.addEventListener('load', function () {
  //Recuperation de la variable des données
  mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
  console.log(mydata);
  data = document.getElementById('EPS111-note');
  console.log(data);
  data.innerHTML = mydata[0][0]["note_Examen"]; //Génération dynamique du tableau de bulletin

  function GenerateBull() {
    /**
     * HEADER
     */
    //title
    var br = document.createElement('br');
    var slogan = document.createElement('div');
    slogan.innerHTML = "Au-del\xE0 de la limite";
    slogan.setAttribute('class', 'slogan');
    var titleinfo = document.createElement('div');
    titleinfo.innerHTML = "BP : 7403 Yaound\xE9  T\xE9l : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfran\xE7oisembango.com Email : isep_fm@yahoo.com";
    titleinfo.setAttribute('class', 'title-info');
    var title = document.createElement('div');
    title.setAttribute("id", "title");
    title.appendChild(slogan);
    title.appendChild(titleinfo); //Logo

    var headleft = document.createElement('div');
    headleft.setAttribute('id', 'head-left');
    var image = document.createElement('img');
    image.setAttribute("src", "/static/bulletin/image/logo.jpeg");
    image.setAttribute("alt", "logo");
    var logo = document.createElement('div');
    logo.setAttribute("id", "logo");
    logo.appendChild(image);
    var headright = document.createElement('div');
    headright.setAttribute('id', 'head-right');
    var containertitle = document.createElement('div');
    containertitle.appendChild(headleft);
    containertitle.appendChild(logo);
    containertitle.appendChild(headright);
    var logoTitle = document.createElement('div');
    logoTitle.setAttribute('id', 'logo-title');
    logoTitle.appendChild(containertitle);
    logoTitle.appendChild(title);
    var header = document.createElement('header');
    header.appendChild(logoTitle);
    body = document.getElementsByTagName('body');
    body[0].appendChild(header);
    var hr = document.createElement('hr');
    /**
     * MAIN
     */

    var bullcheck = document.createElement('div');
    bullcheck.setAttribute('id', 'bull-check');
    bullcheck.innerHTML = "DAF/SER/DFF/FFFF/FFFF";
    var bulltitle = document.createElement('div');
    bulltitle.setAttribute('id', 'bull-title');
    bulltitle.innerHTML = "BULLETIN DE NOTES DU SEMESTRE 1";
    var bullchecktitle = document.createElement('div');
    bullchecktitle.setAttribute('id', 'bull-check-title');
    bullchecktitle.appendChild(bullcheck);
    bullchecktitle.appendChild(bulltitle); //info student

    var info1 = document.createElement('div');
    info1.setAttribute('class', 'info-student-style');
    info1.innerHTML = "Fili\xE8re &nbsp;&nbsp;: ";
    var info2 = document.createElement('div');
    info2.setAttribute('class', 'info-student-style');
    info2.innerHTML = "Sp\xE9cialit\xE9 &nbsp;:  ";
    var info3 = document.createElement('div');
    info3.setAttribute('class', 'info-student-style');
    info3.innerHTML = "Nom (s) &nbsp; &nbsp; : ";
    var info4 = document.createElement('div');
    info4.setAttribute('class', 'info-student-style');
    info4.innerHTML = "Pr\xE9nom (s) : ";
    var info5 = document.createElement('div');
    info5.setAttribute('class', 'info-student-style');
    info5.innerHTML = "Nationalit\xE9 : ";
    var infostudent1 = document.createElement('div');
    infostudent1.setAttribute('id', 'info-student-1');
    infostudent1.appendChild(info1);
    infostudent1.appendChild(info2);
    infostudent1.appendChild(info3);
    infostudent1.appendChild(info4);
    infostudent1.appendChild(info5);
    var info11 = document.createElement('div');
    info11.setAttribute('class', 'info-student-style');
    info11.innerHTML = "Grade : BTS  ";
    var info22 = document.createElement('div');
    info22.setAttribute('class', 'info-student-style');
    info22.innerHTML = "Matricule : ";
    var info33 = document.createElement('div');
    info33.setAttribute('class', 'info-student-style');
    info33.innerHTML = "Date De Naissance : ";
    var info44 = document.createElement('div');
    info44.setAttribute('class', 'info-student-style');
    info44.innerHTML = "Lieu De Naissance : ";
    var info55 = document.createElement('div');
    info55.setAttribute('class', 'info-student-style');
    info55.innerHTML = "Ann\xE9e Acad\xE9mique : ";
    var infostudent2 = document.createElement('div');
    infostudent2.setAttribute('id', 'info-student-2');
    infostudent2.appendChild(info11);
    infostudent2.appendChild(info22);
    infostudent2.appendChild(info33);
    infostudent2.appendChild(info44);
    infostudent2.appendChild(info55);
    var info111 = document.createElement('div');
    info111.innerHTML = "Niveau: I";
    var infostudent3 = document.createElement('div');
    infostudent3.setAttribute('id', 'info-student-3');
    infostudent3.appendChild(info111);
    var infostudent = document.createElement('div');
    infostudent.setAttribute('id', 'info-student');
    infostudent.appendChild(infostudent1);
    infostudent.appendChild(infostudent2);
    infostudent.appendChild(infostudent3);
    /**
     * SEMESTER RESULT
     */
    //table1
    //thead -Line 1

    var tr1 = document.createElement('tr');
    var thvalue = ["", "Groupe UE", "Code UE", "Matière", "Note", "Coef", "Total", "Moyenne Groupe", "Rang", "Mention", "Session", "Crédits Obtenus"];

    for (i = 0; i < thvalue.length; i++) {
      var th = document.createElement('th');
      th.setAttribute("scope", "col");
      th.innerHTML = thvalue[i];
      tr1.appendChild(th);
    }

    var thead1 = document.createElement('thead');
    thead1.appendChild(tr1); //tbody
    //Line 2

    var th1 = document.createElement('th');
    th1.setAttribute('id', 'semestre');
    th1.setAttribute('rowspan', '10');
    th1.innerHTML = "SEMESTRE 1";
    var th2 = document.createElement('th');
    th2.setAttribute('scope', 'row');
    th2.setAttribute('rowspan', '2');
    th2.innerHTML = "UE Fondamentales";
    var td1 = document.createElement('td');
    td1.setAttribute('id', 'EPS111-codeue');
    td1.innerHTML = "EPS111";
    var td2 = document.createElement('td');
    td2.setAttribute('id', 'EPS111-matiere');
    td2.innerHTML = "Histoire et principes de base de l'\xE9ducation Physique";
    var td3 = document.createElement('td');
    td3.setAttribute('id', 'EPS111-note');
    var td4 = document.createElement('td');
    td4.setAttribute('id', 'EPS111-coef');
    var td5 = document.createElement('td');
    td5.setAttribute('id', 'EPS111-total');
    var td6 = document.createElement('td');
    td6.setAttribute('id', 'EPS111-moyenne');
    td6.setAttribute('rowspan', '2');
    var td7 = document.createElement('td');
    td7.setAttribute('id', 'EPS111-rang');
    var td8 = document.createElement('td');
    td8.setAttribute('id', 'EPS111-mention');
    var td9 = document.createElement('td');
    td9.setAttribute('id', 'EPS111-session');
    var td10 = document.createElement('td');
    td10.setAttribute('id', 'EPS111-credits');
    var tr2 = document.createElement('tr');
    tr2.appendChild(th1);
    tr2.appendChild(th2);
    tr2.appendChild(td1);
    tr2.appendChild(td2);
    tr2.appendChild(td3);
    tr2.appendChild(td4);
    tr2.appendChild(td5);
    tr2.appendChild(td6);
    tr2.appendChild(td7);
    tr2.appendChild(td8);
    tr2.appendChild(td9);
    tr2.appendChild(td10); //Line 3

    var td11 = document.createElement('td');
    td11.setAttribute('id', 'EPS112-codeue');
    td11.innerHTML = "EPS 112";
    var td12 = document.createElement('td');
    td12.setAttribute('id', 'EPS112-matiere');
    td12.innerHTML = "Psychologie du Sport-Sociologie du Sport";
    var td13 = document.createElement('td');
    td13.setAttribute('id', 'EPS112-note');
    var td14 = document.createElement('td');
    td14.setAttribute('id', 'EPS112-coef');
    var td15 = document.createElement('td');
    td15.setAttribute('id', 'EPS112-total');
    var td16 = document.createElement('td');
    td16.setAttribute('id', 'EPS112-rang');
    var td17 = document.createElement('td');
    td17.setAttribute('id', 'EPS112-mention');
    var td18 = document.createElement('td');
    td18.setAttribute('id', 'EPS112-session');
    var td19 = document.createElement('td');
    td19.setAttribute('id', 'EPS112-credits');
    var tr3 = document.createElement('tr');
    tr3.appendChild(td11);
    tr3.appendChild(td12);
    tr3.appendChild(td13);
    tr3.appendChild(td14);
    tr3.appendChild(td15);
    tr3.appendChild(td16);
    tr3.appendChild(td17);
    tr3.appendChild(td18);
    tr3.appendChild(td19); //Line 4

    var th2 = document.createElement('td');
    th2.setAttribute('scope', 'row');
    th2.setAttribute('rowspan', '4');
    th2.innerHTML = "UE Professionnelles";
    var td20 = document.createElement('td');
    td20.setAttribute("id", "EPS113-codeue");
    td20.innerHTML = "EPS113";
    var td21 = document.createElement('td');
    td21.setAttribute("id", "EPS113-matiere");
    td21.innerHTML = "Didactique De l'EPS I";
    var td22 = document.createElement('td');
    td22.setAttribute("id", "EPS113-note");
    var td22 = document.createElement('td');
    td22.setAttribute("id", "EPS113-coef");
    var td23 = document.createElement('td');
    td23.setAttribute("id", "EPS113-total");
    var td24 = document.createElement('td');
    td24.setAttribute("rowspan", "4");
    td24.setAttribute("id", "EPS113-moyenne");
    var td25 = document.createElement('td');
    td25.setAttribute("id", "EPS113-rang");
    var td26 = document.createElement('td');
    td26.setAttribute("id", "EPS113-mention");
    var td27 = document.createElement('td');
    td27.setAttribute("id", "EPS113-session");
    var td28 = document.createElement('td');
    td28.setAttribute("id", "EPS113-credits");
    var tr4 = document.createElement('tr');
    tr4.appendChild(td20);
    tr4.appendChild(td21);
    tr4.appendChild(td22);
    tr4.appendChild(td23);
    tr4.appendChild(td24);
    tr4.appendChild(td25);
    tr4.appendChild(td26);
    tr4.appendChild(td27);
    tr4.appendChild(td28); //tbody

    var tbody = document.createElement('tbody');
    tbody.appendChild(tr2);
    tbody.appendChild(tr3);
    tbody.appendChild(tr4);
    var table1 = document.createElement('table');
    table1.setAttribute('class', 'table-1');
    table1.appendChild(thead1);
    table1.appendChild(tbody); //semester Result

    var semestreResult = document.createElement('div');
    semestreResult.setAttribute('id', 'semester-result');
    semestreResult.appendChild(table1); //Main

    var main = document.createElement('main');
    main.appendChild(bullchecktitle);
    main.appendChild(infostudent);
    main.appendChild(semestreResult); //TEST

    containerbull = document.createElement('div');
    containerbull.setAttribute('class', 'container-bull');
    containerbull.appendChild(header);
    containerbull.appendChild(hr);
    containerbull.appendChild(main); //TEST

    body = document.getElementsByTagName('body');
    body[0].appendChild(containerbull);
  }

  GenerateBull();
});