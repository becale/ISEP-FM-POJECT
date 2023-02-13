"use strict";

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance"); }

function _iterableToArray(iter) { if (Symbol.iterator in Object(iter) || Object.prototype.toString.call(iter) === "[object Arguments]") return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = new Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } }

window.addEventListener('load', function () {
  //Recuperation de la variable des données
  mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
  console.log(mydata); //Génération dynamique du tableau de bulletin
  //TEST GENERAL POUR TOUS LES BULLETINS SEMESTRE  1 3 5S

  body = document.getElementById('body');

  if (mydata[0] == 'GESTION') {
    moY = [];
    containerrr = GenerateBullMDS1Semestre1();
    listcontainer = document.createElement('div');

    for (i = 0; i < mydata[1].length; i++) {
      clone = containerrr.cloneNode(true); //Execution des traitements sur container

      clone = BullMDS1(clone);
      /**MOYENNE */

      moY[i] = globalThis.resultat.children[3].innerHTML; //console.log(moY);
      //Puis ajout au containerList

      listcontainer.appendChild(clone);
    } //Fixation de ContainerList sur le body de la page


    body.appendChild(listcontainer);
    moY = stringToIntArray(moY);
    moy = triDecroissant(moY);
    console.log(moy);
  } else if (mydata[0] == 'STAPS1') {
    containeer = GenerateBullStaps1Semestre1();
    listcontainer = document.createElement('div');

    for (i = 0; i < mydata[1].length; i++) {
      clone = containeer.cloneNode(true); //Execution des traitements sur container

      clone = BullSTAPS1(clone, i); //Puis ajout au containerList

      listcontainer.appendChild(clone);
    } //Fixation de ContainerList sur le body de la page


    body.appendChild(listcontainer);
  } else if (mydata[0] == 'STAPS2') {
    body = document.getElementById('body');
    containeer = GenerateBullStaps2Semestre3();
    listcontainer = document.createElement('div');

    for (i = 0; i < mydata[1].length; i++) {
      clone = containeer.cloneNode(true); //Execution des traitements sur container
      //clone = BullMDS1(clone)
      //Puis ajout au containerList

      listcontainer.appendChild(clone);
    } //Fixation de ContainerList sur le body de la page


    body.appendChild(listcontainer);
  } else if (mydata[0] == 'EVENEMENTIEL') {
    containeer = GenerateBullEVEsemestre5();
    listcontainer = document.createElement('div'); //for(i=0; i<mydata[1].length; i++){

    clone = containeer.cloneNode(true); //Execution des traitements sur container
    //clone = BullMDS1(clone)
    //Puis ajout au containerList

    listcontainer.appendChild(clone); //}
    //Fixation de ContainerList sur le body de la page

    var body = document.getElementById('body');
    body.appendChild(listcontainer);
  } else if (mydata[0] == 'MSO') {
    containeer = GenerateBullMSOsemestre5();
    listcontainer = document.createElement('div'); //for(i=0; i<mydata[1].length; i++){

    clone = containeer.cloneNode(true); //Execution des traitements sur container
    //clone = BullMDS1(clone)
    //Puis ajout au containerList

    listcontainer.appendChild(clone); //}
    //Fixation de ContainerList sur le body de la page

    body.appendChild(listcontainer);
  }
});
/**
 * DECLARATION DES FONCTIONS DE GENERATION DES BULLETTINS DES SEMESTRES 1, 3, 5
 */

/*DECLARATION S1 MDS*/

function GenerateBullMDS1Semestre1() {
  //title
  var br = document.createElement('br');
  var slogan = document.createElement('div');
  slogan.innerHTML = "Au-del\xE0 de la limite";
  slogan.setAttribute('class', 'slogan');
  var titleinfo = document.createElement('div');
  titleinfo.innerHTML = "BP : 7403 Yaound\xE9  T\xE9l : (237) 695 548 821 / 653 764 050 <br> Site Web : www.institutfran\xE7oisembango.com Email : isep_fm@yahoo.com";
  titleinfo.setAttribute('class', 'title-info');
  title = document.createElement('div');
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
  containertitle = document.createElement('div');
  containertitle.appendChild(headleft);
  containertitle.appendChild(logo);
  containertitle.appendChild(headright);
  logoTitle = document.createElement('div');
  logoTitle.setAttribute('id', 'logo-title');
  logoTitle.appendChild(containertitle);
  logoTitle.appendChild(title);
  header = document.createElement('div');
  header.appendChild(logoTitle);
  hr = document.createElement('hr');
  first = document.createElement('div');
  first.appendChild(header);
  first.appendChild(hr); //MAIN

  var bullcheck = document.createElement('div');
  bullcheck.setAttribute('id', 'bull-check');
  bullcheck.innerHTML = "DAF/SG/DE/PR";
  var bulltitle = document.createElement('div');
  bulltitle.setAttribute('id', 'bull-title');
  bulltitle.innerHTML = "BULLETIN DE NOTES SEMESTRE 1";
  var bullchecktitle = document.createElement('div');
  bullchecktitle.setAttribute('id', 'bull-check-title');
  bullchecktitle.appendChild(bullcheck);
  bullchecktitle.appendChild(bulltitle); //info student

  var info1 = document.createElement('div');
  info1.setAttribute('class', 'info-student-style');
  info1.innerHTML = "Fili\xE8re &nbsp;&nbsp; : GESTION";
  var info2 = document.createElement('div');
  info2.setAttribute('class', 'info-student-style');
  info2.innerHTML = "Sp\xE9cialit\xE9 &nbsp;:  MDS";
  var info3 = document.createElement('div');
  info3.setAttribute('class', 'info-student-style');
  info3.innerHTML = "Nom (s) &nbsp; &nbsp; : ";
  var info4 = document.createElement('div');
  info4.setAttribute('class', 'info-student-style');
  info4.innerHTML = "Pr\xE9nom (s) : ";
  var info5 = document.createElement('div');
  info5.setAttribute('class', 'info-student-style');
  info5.innerHTML = "Nationalit\xE9 : Camerounais(e)";
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
  infostudent.appendChild(infostudent3); //table1
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
  th1.setAttribute('rowspan', '11');
  th1.innerHTML = "SEMESTRE 1";
  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '4');
  th2.innerHTML = "UE Fondamentales";
  var td1 = document.createElement('td');
  td1.setAttribute('id', 'MDS111-codeue');
  td1.innerHTML = "MDS111";
  var td2 = document.createElement('td');
  td2.setAttribute('id', 'MDS111-matiere');
  td2.innerHTML = "Math\xE9matiques I";
  var td3 = document.createElement('td');
  td3.setAttribute('id', 'MDS111-note');
  var td4 = document.createElement('td');
  td4.setAttribute('id', 'MDS111-coef');
  var td5 = document.createElement('td');
  td5.setAttribute('id', 'MDS111-total');
  var td6 = document.createElement('td');
  td6.setAttribute('id', 'MDS111-moyenne');
  td6.setAttribute('rowspan', '4');
  var td7 = document.createElement('td');
  td7.setAttribute('id', 'MDS111-rang');
  var td8 = document.createElement('td');
  td8.setAttribute('id', 'MDS111-mention');
  var td9 = document.createElement('td');
  td9.setAttribute('id', 'MDS111-session');
  var td10 = document.createElement('td');
  td10.setAttribute('id', 'MDS111-credits');
  td10.setAttribute('rowspan', '2');
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

  var td1 = document.createElement('td');
  td1.setAttribute('id', 'MDS111-codeue');
  td1.innerHTML = "MDS111";
  var td2 = document.createElement('td');
  td2.setAttribute('id', 'MDS111-matiere');
  td2.innerHTML = "Informatique I";
  var td3 = document.createElement('td');
  td3.setAttribute('id', 'MDS111-note');
  var td4 = document.createElement('td');
  td4.setAttribute('id', 'MDS111-coef');
  var td5 = document.createElement('td');
  td5.setAttribute('id', 'MDS111-total');
  var td6 = document.createElement('td');
  td6.setAttribute('id', 'MDS111-rang');
  var td7 = document.createElement('td');
  td7.setAttribute('id', 'MDS111-mention');
  var td8 = document.createElement('td');
  td8.setAttribute('id', 'MDS111-session');
  /*var td9=document.createElement('td')
  td9.setAttribute('id','MDS111-credits')*/

  var tr3 = document.createElement('tr');
  tr3.appendChild(td1);
  tr3.appendChild(td2);
  tr3.appendChild(td3);
  tr3.appendChild(td4);
  tr3.appendChild(td5);
  tr3.appendChild(td6);
  tr3.appendChild(td7);
  tr3.appendChild(td8);
  /* tr3.appendChild(td9)*/
  //Line 33

  var td11 = document.createElement('td');
  td11.setAttribute('id', 'MDS112-codeue');
  td11.innerHTML = "MDS112";
  var td12 = document.createElement('td');
  td12.setAttribute('id', 'MDS112-matiere');
  td12.innerHTML = "Math\xE9matiques Financi\xE8res";
  var td13 = document.createElement('td');
  td13.setAttribute('id', 'MDS112-note');
  var td14 = document.createElement('td');
  td14.setAttribute('id', 'MDS112-coef');
  var td15 = document.createElement('td');
  td15.setAttribute('id', 'MDS112-total');
  /*var td166=document.createElement('td')
  td166.setAttribute('id','MDS112-moyenne')*/

  var td16 = document.createElement('td');
  td16.setAttribute('id', 'MDS112-rang');
  var td17 = document.createElement('td');
  td17.setAttribute('id', 'MDS112-mention');
  var td18 = document.createElement('td');
  td18.setAttribute('id', 'MDS112-session');
  var td19 = document.createElement('td');
  td19.setAttribute('id', 'MDS112-credits');
  td19.setAttribute('rowspan', '2');
  var tr33 = document.createElement('tr');
  tr33.setAttribute('id', 'tr33-border-top');
  tr33.appendChild(td11);
  tr33.appendChild(td12);
  tr33.appendChild(td13);
  tr33.appendChild(td14);
  tr33.appendChild(td15); //tr33.appendChild(td166)

  tr33.appendChild(td16);
  tr33.appendChild(td17);
  tr33.appendChild(td18);
  tr33.appendChild(td19); //Line 333

  var td111 = document.createElement('td');
  td111.setAttribute('id', 'MDS112-codeue');
  td111.innerHTML = "MDS112";
  var td122 = document.createElement('td');
  td122.setAttribute('id', 'MDS112-matiere');
  td122.innerHTML = "Statistiques Descriptives";
  var td133 = document.createElement('td');
  td133.setAttribute('id', 'MDS112-note');
  var td144 = document.createElement('td');
  td144.setAttribute('id', 'MDS112-coef');
  var td155 = document.createElement('td');
  td155.setAttribute('id', 'MDS112-total');
  /*var td166=document.createElement('td')
  td166.setAttribute('id','MDS112-moyenne')*/

  var td166 = document.createElement('td');
  td166.setAttribute('id', 'MDS112-rang');
  var td177 = document.createElement('td');
  td177.setAttribute('id', 'MDS112-mention');
  var td188 = document.createElement('td');
  td188.setAttribute('id', 'MDS112-session');
  /*var td199=document.createElement('td')
  td199.setAttribute('id','MDS112-credits')*/

  var tr333 = document.createElement('tr');
  tr333.setAttribute('id', 'tr333-border-top');
  tr333.appendChild(td111);
  tr333.appendChild(td122);
  tr333.appendChild(td133);
  tr333.appendChild(td144);
  tr333.appendChild(td155); //tr33.appendChild(td166)

  tr333.appendChild(td166);
  tr333.appendChild(td177);
  tr333.appendChild(td188); //tr333.appendChild(td199)
  //Line 4 //REGROUPER L4 et L5 dans une boucle

  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '4');
  th2.innerHTML = "UE Professionnelles";
  var td20 = document.createElement('td');
  td20.setAttribute("id", "MDS113-codeue");
  td20.innerHTML = "MDS113";
  var td21 = document.createElement('td');
  td21.setAttribute("id", "MDS113-matiere");
  td21.innerHTML = "Environnement Jurique Et Comptable I";
  var td22 = document.createElement('td');
  td22.setAttribute("id", "MDS113-note");
  var td222 = document.createElement('td');
  td222.setAttribute("id", "MDS113-coef");
  var td23 = document.createElement('td');
  td23.setAttribute("id", "MDS113-total");
  var td24 = document.createElement('td');
  td24.setAttribute("rowspan", "4");
  td24.setAttribute("id", "MDS113-moyenne");
  var td25 = document.createElement('td');
  td25.setAttribute("id", "MDS113-rang");
  var td26 = document.createElement('td');
  td26.setAttribute("id", "MDS113-mention");
  var td27 = document.createElement('td');
  td27.setAttribute("id", "MDS113-session");
  var td28 = document.createElement('td');
  td28.setAttribute("id", "MDS113-credits");
  var tr4 = document.createElement('tr');
  tr4.appendChild(th2);
  tr4.appendChild(td20);
  tr4.appendChild(td21);
  tr4.appendChild(td22);
  tr4.appendChild(td222);
  tr4.appendChild(td23);
  tr4.appendChild(td24);
  tr4.appendChild(td25);
  tr4.appendChild(td26);
  tr4.appendChild(td27);
  tr4.appendChild(td28); //Line 5

  var td28 = document.createElement('td');
  td28.setAttribute("id", "MDS114-codeue");
  td28.innerHTML = "MDS114";
  var td29 = document.createElement('td');
  td29.setAttribute("id", "MDS114-matiere");
  td29.innerHTML = "Marketing";
  var td30 = document.createElement('td');
  td30.setAttribute("id", "MDS114-note");
  var td31 = document.createElement('td');
  td31.setAttribute("id", "MDS114-coef");
  var td32 = document.createElement('td');
  td32.setAttribute("id", "MDS114-total");
  var td33 = document.createElement('td');
  td33.setAttribute("id", "MDS114-rang");
  var td34 = document.createElement('td');
  td34.setAttribute("id", "MDS114-mention");
  var td35 = document.createElement('td');
  td35.setAttribute("id", "MDS114-session");
  var td36 = document.createElement('td');
  td36.setAttribute("id", "MDS114-credits");
  var tr5 = document.createElement('tr');
  tr5.appendChild(td28);
  tr5.appendChild(td29);
  tr5.appendChild(td30);
  tr5.appendChild(td31);
  tr5.appendChild(td32);
  tr5.appendChild(td33);
  tr5.appendChild(td34);
  tr5.appendChild(td35);
  tr5.appendChild(td36); //Line 6

  var td377 = document.createElement('td');
  td377.setAttribute("id", "MDS115-codeue");
  td377.innerHTML = "MDS115";
  var td37 = document.createElement('td');
  td37.setAttribute("id", "MDS115-matiere");
  td37.innerHTML = "Outils De Gestion Du Sport I";
  var td38 = document.createElement('td');
  td38.setAttribute("id", "MDS115-note");
  var td39 = document.createElement('td');
  td39.setAttribute("id", "MDS115-coef");
  var td40 = document.createElement('td');
  td40.setAttribute("id", "MDS115-total");
  var td41 = document.createElement('td');
  td41.setAttribute("id", "MDS115-rang");
  var td42 = document.createElement('td');
  td42.setAttribute("id", "MDS115-mention");
  var td43 = document.createElement('td');
  td43.setAttribute("id", "MDS115-session");
  var td44 = document.createElement('td');
  td44.setAttribute("id", "MDS115-credits");
  var tr6 = document.createElement('tr');
  tr6.appendChild(td377);
  tr6.appendChild(td37);
  tr6.appendChild(td38);
  tr6.appendChild(td39);
  tr6.appendChild(td40);
  tr6.appendChild(td41);
  tr6.appendChild(td42);
  tr6.appendChild(td43);
  tr6.appendChild(td44); //Line 7

  var td45 = document.createElement('td');
  td45.setAttribute("id", "MDS116-codeue");
  td45.innerHTML = "MDS116";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "MDS116-matiere");
  td46.innerHTML = "Gestion Des Structures Et organisation Sportives I";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "MDS116-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "MDS116-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "MDS116-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "MDS116-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "MDS116-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "MDS116-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "MDS116-credits");
  var tr7 = document.createElement('tr');
  tr7.appendChild(td45);
  tr7.appendChild(td46);
  tr7.appendChild(td47);
  tr7.appendChild(td48);
  tr7.appendChild(td49);
  tr7.appendChild(td50);
  tr7.appendChild(td51);
  tr7.appendChild(td52);
  tr7.appendChild(td53); //Line 8

  var th3 = document.createElement('th');
  th3.setAttribute('scope', 'row');
  th3.setAttribute('rowspan', '2');
  th3.innerHTML = "UE Transversales";
  var td54 = document.createElement('td');
  td54.setAttribute("id", "MDS117-codeue");
  td54.innerHTML = "MDS117";
  var td56 = document.createElement('td');
  td56.setAttribute("id", "MDS117-matiere");
  td56.innerHTML = "Technique D'Expression Anglaise";
  var td57 = document.createElement('td');
  td57.setAttribute("id", "MDS117-note");
  var td58 = document.createElement('td');
  td58.setAttribute("id", "MDS117-coef");
  var td59 = document.createElement('td');
  td59.setAttribute("id", "MDS117-total");
  var td60 = document.createElement('td'); //td60.setAttribute("rowspan","3")

  td60.setAttribute("id", "MDS117-moyenne");
  td60.setAttribute('rowspan', '2');
  var td61 = document.createElement('td');
  td61.setAttribute("id", "MDS117-rang");
  var td62 = document.createElement('td');
  td62.setAttribute("id", "MDS117-mention");
  var td63 = document.createElement('td');
  td63.setAttribute("id", "MDS117-session");
  var td64 = document.createElement('td');
  td64.setAttribute("id", "MDS117-credits");
  td64.setAttribute("rowspan", "2");
  var tr8 = document.createElement('tr');
  tr8.appendChild(th3);
  tr8.appendChild(td54);
  tr8.appendChild(td56);
  tr8.appendChild(td57);
  tr8.appendChild(td58);
  tr8.appendChild(td59);
  tr8.appendChild(td60);
  tr8.appendChild(td61);
  tr8.appendChild(td62);
  tr8.appendChild(td63);
  tr8.appendChild(td64); //Line 88

  /*var th3=document.createElement('th')
  th3.setAttribute('scope','row')
  //th3.setAttribute('rowspan','3')
  th3.innerHTML=`UE Transversales`*/

  var td544 = document.createElement('td');
  td544.setAttribute("id", "MDS117-codeue");
  td544.innerHTML = "MDS117";
  var td566 = document.createElement('td');
  td566.setAttribute("id", "MDS117-matiere");
  td566.innerHTML = "Technique D'Expression Fran\xE7aise";
  var td577 = document.createElement('td');
  td577.setAttribute("id", "MDS117-note");
  var td588 = document.createElement('td');
  td588.setAttribute("id", "MDS117-coef");
  var td599 = document.createElement('td');
  td599.setAttribute("id", "MDS117-total"); //var td600=document.createElement('td')
  //td60.setAttribute("rowspan","3")
  //td600.setAttribute("id","MDS117-moyenne")

  var td611 = document.createElement('td');
  td611.setAttribute("id", "MDS117-rang");
  var td622 = document.createElement('td');
  td622.setAttribute("id", "MDS117-mention");
  var td633 = document.createElement('td');
  td633.setAttribute("id", "MDS117-session");
  /*var td644=document.createElement('td')
  td644.setAttribute("id","MDS117-credits")*/

  var tr88 = document.createElement('tr'); //tr88.appendChild(th3)

  tr88.appendChild(td544);
  tr88.appendChild(td566);
  tr88.appendChild(td577);
  tr88.appendChild(td588);
  tr88.appendChild(td599); //tr88.appendChild(td600)

  tr88.appendChild(td611);
  tr88.appendChild(td622);
  tr88.appendChild(td633); //tr88.appendChild(td644)
  //Line 9

  var tr9 = document.createElement('tr'); //tr9.setAttribute('id','resultat-eps2')

  for (i = 0; i <= 6; i++) {
    var td = document.createElement('td');

    if (i == 0) {
      td.innerHTML = "RESULTATS SEMESTRE 1";
      td.setAttribute('colspan', '4');
    }

    if (i == 1) {
      td.setAttribute('id', 'resultat-coef');
    }

    if (i == 2) {
      td.setAttribute('id', 'resultat-total');
    }

    if (i == 3) {
      td.setAttribute('id', 'resultat-moyenne');
    }

    if (i == 4) {
      td.setAttribute('id', 'resultat-rang');
    }

    if (i == 5) {
      td.setAttribute('id', 'resultat');
      td.setAttribute('colspan', '2');
      td.innerHTML = "Total Cr\xE9dits Semestre 1";
    }

    if (i == 6) {
      td.setAttribute('id', 'resultat-crédits');
    }

    tr9.appendChild(td);
  } //tbody


  var tbody = document.createElement('tbody');
  tbody.setAttribute('id', 'tbody00');
  tbody.appendChild(tr2);
  tbody.appendChild(tr3);
  tbody.appendChild(tr33);
  tbody.appendChild(tr333);
  tbody.appendChild(tr4);
  tbody.appendChild(tr5);
  tbody.appendChild(tr6);
  tbody.appendChild(tr7);
  tbody.appendChild(tr8);
  tbody.appendChild(tr88);
  tbody.appendChild(tr9);
  var table1 = document.createElement('table');
  table1.setAttribute('class', 'table-1');
  table1.appendChild(thead1);
  table1.appendChild(tbody); //table3
  //thead2

  var tr12 = document.createElement('tr');

  for (i = 0; i <= 11; i++) {
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');

    if (i == 0) {
      th.innerHTML = "&nbsp;&nbsp;";
    }

    tr12.appendChild(th);
  }

  var thead2 = document.createElement('thead');
  thead2.appendChild(tr12); //tbody
  //Line 1

  var tr13 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne de Classe de l'\xE9tudiant :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Maximum :";
    }

    if (i == 7) {
      td.innerHTML = "Retard :";
    }

    tr13.appendChild(td);
  } //Line 2


  var tr14 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne G\xE9n\xE9rale de la classe :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Minimum :";
    }

    if (i == 7) {
      td.innerHTML = "Absences:";
    }

    tr14.appendChild(td);
  } //Line 3


  var tr15 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      /*td.innerHTML=`Moyenne Générale de la classe :`*/
    } //if(i==3){/*td.innerHTML=`/ 20`*/}


    if (i == 4) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Rang :";
    } //if(i==8){td.innerHTML=`Absences:`}


    if (i == 5) {
      td.innerHTML = " sur ";
    }

    tr15.appendChild(td);
  } //Line 4
  //TABLEAU 3


  var tbody3 = document.createElement('tbody');
  tbody3.setAttribute('id', 'tbody-3');
  tbody3.appendChild(tr13);
  tbody3.appendChild(tr14);
  tbody3.appendChild(tr15);
  var table3 = document.createElement('table');
  table3.setAttribute('id', 'table-3');
  table3.appendChild(thead2);
  table3.appendChild(tbody3); //semester Result

  var semestreResult = document.createElement('div');
  semestreResult.setAttribute('id', 'semester-result');
  semestreResult.appendChild(table1);
  semestreResult.appendChild(table3); //Main

  var main = document.createElement('main');
  main.appendChild(bullchecktitle);
  main.appendChild(infostudent);
  main.appendChild(semestreResult); //Footer

  var visa = document.createElement('div');
  visa.setAttribute('class', 'visa');
  visa.innerHTML = "VISA CHEF ETABLISSEMENT";
  var footer = document.createElement('footer');
  footer.appendChild(visa); //TEST

  containerbull = document.createElement('div');
  containerbull.setAttribute('class', 'container-bull');
  containerbull.appendChild(header);
  containerbull.appendChild(hr);
  containerbull.appendChild(main);
  containerbull.appendChild(footer); //Retour Du composant Bulletin

  return containerbull;
}
/*DECLARATION S1 STAPS*/


function GenerateBullStaps1Semestre1() {
  var br = document.createElement('br');
  var slogan = document.createElement('div');
  slogan.innerHTML = "ARRETE N022-0003/L/MINESUP/DDES/ESUP/SDA/ABC";
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
  var body = document.getElementsByTagName('body');
  body[0].appendChild(header);
  var hr = document.createElement('hr'); //MAIN

  var bullcheck = document.createElement('div');
  bullcheck.setAttribute('id', 'bull-check');
  bullcheck.innerHTML = "DAF/SG/DE/PR";
  var bulltitle = document.createElement('div');
  bulltitle.setAttribute('id', 'bull-title');
  bulltitle.innerHTML = "BULLETIN DE NOTES SEMESTRE 1";
  var bullchecktitle = document.createElement('div');
  bullchecktitle.setAttribute('id', 'bull-check-title');
  bullchecktitle.appendChild(bullcheck);
  bullchecktitle.appendChild(bulltitle); //info student

  var info1 = document.createElement('div');
  info1.setAttribute('class', 'info-student-style');
  info1.innerHTML = "Fili\xE8re &nbsp;&nbsp; : STAPS";
  var info2 = document.createElement('div');
  info2.setAttribute('class', 'info-student-style');
  info2.innerHTML = "Sp\xE9cialit\xE9 &nbsp;:  EPS";
  var info3 = document.createElement('div');
  info3.setAttribute('class', 'info-student-style');
  info3.innerHTML = "Nom (s) &nbsp; &nbsp; : ";
  var info4 = document.createElement('div');
  info4.setAttribute('class', 'info-student-style');
  info4.innerHTML = "Pr\xE9nom (s) : ";
  var info5 = document.createElement('div');
  info5.setAttribute('class', 'info-student-style');
  info5.innerHTML = "Nationalit\xE9 : Camerounais(e)";
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
  infostudent.appendChild(infostudent3); //table1
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
  th1.setAttribute('rowspan', '13');
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
  td11.innerHTML = "EPS112";
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
  tr3.appendChild(td19); //Line 4 //REGROUPER L4 et L5 dans une boucle

  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '7');
  th2.innerHTML = "UE Professionnelles";
  var td20 = document.createElement('td');
  td20.setAttribute("id", "EPS113-codeue");
  td20.innerHTML = "EPS113";
  var td21 = document.createElement('td');
  td21.setAttribute("id", "EPS113-matiere");
  td21.innerHTML = "Didactique De l'EPS I";
  var td22 = document.createElement('td');
  td22.setAttribute("id", "EPS113-note");
  var td222 = document.createElement('td');
  td222.setAttribute("id", "EPS113-coef");
  var td23 = document.createElement('td');
  td23.setAttribute("id", "EPS113-total");
  var td24 = document.createElement('td');
  td24.setAttribute("rowspan", "7");
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
  tr4.appendChild(th2);
  tr4.appendChild(td20);
  tr4.appendChild(td21);
  tr4.appendChild(td22);
  tr4.appendChild(td222);
  tr4.appendChild(td23);
  tr4.appendChild(td24);
  tr4.appendChild(td25);
  tr4.appendChild(td26);
  tr4.appendChild(td27);
  tr4.appendChild(td28); //Line 5

  var td28 = document.createElement('td');
  td28.setAttribute("id", "EPS114-codeue");
  td28.innerHTML = "EPS114";
  var td29 = document.createElement('td');
  td29.setAttribute("id", "EPS114-matiere");
  td29.innerHTML = "Anatomie I";
  var td30 = document.createElement('td');
  td30.setAttribute("id", "EPS114-note");
  var td31 = document.createElement('td');
  td31.setAttribute("id", "EPS114-coef");
  var td32 = document.createElement('td');
  td32.setAttribute("id", "EPS114-total");
  var td33 = document.createElement('td');
  td33.setAttribute("id", "EPS114-rang");
  var td34 = document.createElement('td');
  td34.setAttribute("id", "EPS114-mention");
  var td35 = document.createElement('td');
  td35.setAttribute("id", "EPS114-session");
  var td36 = document.createElement('td');
  td36.setAttribute("id", "EPS114-credits");
  var tr5 = document.createElement('tr');
  tr5.appendChild(td28);
  tr5.appendChild(td29);
  tr5.appendChild(td30);
  tr5.appendChild(td31);
  tr5.appendChild(td32);
  tr5.appendChild(td33);
  tr5.appendChild(td34);
  tr5.appendChild(td35);
  tr5.appendChild(td36); //Line 6

  var td377 = document.createElement('td');
  td377.setAttribute("id", "EPS115a-codeue");
  td377.innerHTML = "EPS115";
  var td37 = document.createElement('td');
  td37.setAttribute("id", "EPS115a-matiere");
  td37.innerHTML = "Didactique des APS: Athl\xE9tisme";
  var td38 = document.createElement('td');
  td38.setAttribute("id", "EPS115a-note");
  var td39 = document.createElement('td');
  td39.setAttribute("id", "EPS115a-coef");
  var td40 = document.createElement('td');
  td40.setAttribute("id", "EPS115a-total");
  var td41 = document.createElement('td');
  td41.setAttribute("id", "EPS115a-rang");
  var td42 = document.createElement('td');
  td42.setAttribute("id", "EPS115a-mention");
  var td43 = document.createElement('td');
  td43.setAttribute("id", "EPS115a-session");
  var td44 = document.createElement('td');
  td44.setAttribute('rowspan', "4");
  td44.setAttribute("id", "EPS115a-credits");
  var tr6 = document.createElement('tr');
  tr6.appendChild(td377);
  tr6.appendChild(td37);
  tr6.appendChild(td38);
  tr6.appendChild(td39);
  tr6.appendChild(td40);
  tr6.appendChild(td41);
  tr6.appendChild(td42);
  tr6.appendChild(td43);
  tr6.appendChild(td44); //Line 6a

  var td377a = document.createElement('td');
  td377a.setAttribute("id", "EPS115-codeue");
  td377a.innerHTML = "EPS115";
  var td37a = document.createElement('td');
  td37a.setAttribute("id", "EPS115b-matiere");
  td37a.innerHTML = "Didactique des APS: Basket Ball";
  var td38a = document.createElement('td');
  td38a.setAttribute("id", "EPS115b-note");
  var td39a = document.createElement('td');
  td39a.setAttribute("id", "EPS115b-coef");
  var td40a = document.createElement('td');
  td40a.setAttribute("id", "EPS115b-total");
  var td41a = document.createElement('td');
  td41a.setAttribute("id", "EPS115b-rang");
  var td42a = document.createElement('td');
  td42a.setAttribute("id", "EPS115b-mention");
  var td43a = document.createElement('td');
  td43a.setAttribute("id", "EPS115b-session"); //var td44a=document.createElement('td')
  //td44a.setAttribute("id","EPS115b-credits")

  var tr6a = document.createElement('tr');
  tr6a.setAttribute('id', 'ligne-EPS115b');
  tr6a.appendChild(td377a);
  tr6a.appendChild(td37a);
  tr6a.appendChild(td38a);
  tr6a.appendChild(td39a);
  tr6a.appendChild(td40a);
  tr6a.appendChild(td41a);
  tr6a.appendChild(td42a);
  tr6a.appendChild(td43a); //tr6a.appendChild(td44a)
  //Line 6b

  var td377b = document.createElement('td');
  td377b.setAttribute("id", "EPS115b-codeue");
  td377b.innerHTML = "EPS115";
  var td37b = document.createElement('td');
  td37b.setAttribute("id", "EPS115b-matiere");
  td37b.innerHTML = "Didactique des APS: Judo";
  var td38b = document.createElement('td');
  td38b.setAttribute("id", "EPS115b-note");
  var td39b = document.createElement('td');
  td39b.setAttribute("id", "EPS115b-coef");
  var td40b = document.createElement('td');
  td40b.setAttribute("id", "EPS115b-total");
  var td41b = document.createElement('td');
  td41b.setAttribute("id", "EPS115b-rang");
  var td42b = document.createElement('td');
  td42b.setAttribute("id", "EPS115b-mention");
  var td43b = document.createElement('td');
  td43b.setAttribute("id", "EPS115b-session");
  var td44b = document.createElement('td'); //td44b.setAttribute("id","EPS115b-credits")

  var tr6b = document.createElement('tr');
  tr6b.appendChild(td377b);
  tr6b.appendChild(td37b);
  tr6b.appendChild(td38b);
  tr6b.appendChild(td39b);
  tr6b.appendChild(td40b);
  tr6b.appendChild(td41b);
  tr6b.appendChild(td42b);
  tr6b.appendChild(td43b); //tr6b.appendChild(td44b)
  //Line 6j

  var td377j = document.createElement('td');
  td377j.setAttribute("id", "EPS115j-codeue");
  td377j.innerHTML = "EPS115";
  var td37j = document.createElement('td');
  td37j.setAttribute("id", "EPS115j-matiere");
  td37j.innerHTML = "Didactique des APS: Lutte";
  var td38j = document.createElement('td');
  td38j.setAttribute("id", "EPS115j-note");
  var td39j = document.createElement('td');
  td39j.setAttribute("id", "EPS115j-coef");
  var td40j = document.createElement('td');
  td40j.setAttribute("id", "EPS115j-total");
  var td41j = document.createElement('td');
  td41j.setAttribute("id", "EPS115j-rang");
  var td42j = document.createElement('td');
  td42j.setAttribute("id", "EPS115j-mention");
  var td43j = document.createElement('td');
  td43j.setAttribute("id", "EPS115j-session"); //var td44j=document.createElement('td')
  //td44j.setAttribute("id","EPS115j-credits")

  var tr6j = document.createElement('tr');
  tr6j.appendChild(td377j);
  tr6j.appendChild(td37j);
  tr6j.appendChild(td38j);
  tr6j.appendChild(td39j);
  tr6j.appendChild(td40j);
  tr6j.appendChild(td41j);
  tr6j.appendChild(td42j);
  tr6j.appendChild(td43j); //tr6j.appendChild(td44j)
  //Line 7

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EPS116-codeue");
  td45.innerHTML = "EPS116";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EPS116-matiere");
  td46.innerHTML = "La Physiologie de l\u2019Execice I";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EPS116-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EPS116-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EPS116-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EPS116-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EPS116-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EPS116-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "EPS116-credits");
  var tr7 = document.createElement('tr');
  tr7.appendChild(td45);
  tr7.appendChild(td46);
  tr7.appendChild(td47);
  tr7.appendChild(td48);
  tr7.appendChild(td49);
  tr7.appendChild(td50);
  tr7.appendChild(td51);
  tr7.appendChild(td52);
  tr7.appendChild(td53); //Line 8

  var th3 = document.createElement('th');
  th3.setAttribute('scope', 'row');
  th3.setAttribute('rowspan', '3');
  th3.innerHTML = "UE Transversales";
  var td54 = document.createElement('td');
  td54.setAttribute("id", "EPS117-codeue");
  td54.innerHTML = "EPS117";
  var td56 = document.createElement('td');
  td56.setAttribute("id", "EPS117-matiere");
  td56.innerHTML = "Informatique";
  var td57 = document.createElement('td');
  td57.setAttribute("id", "EPS117-note");
  var td58 = document.createElement('td');
  td58.setAttribute("id", "EPS117-coef");
  var td59 = document.createElement('td');
  td59.setAttribute("id", "EPS117-total");
  var td60 = document.createElement('td');
  td60.setAttribute("rowspan", "3");
  td60.setAttribute("id", "EPS117-moyenne");
  var td61 = document.createElement('td');
  td61.setAttribute("id", "EPS117-rang");
  var td62 = document.createElement('td');
  td62.setAttribute("id", "EPS117-mention");
  var td63 = document.createElement('td');
  td63.setAttribute("id", "EPS117-session");
  var td64 = document.createElement('td'); //td64.setAttribute('rowspan','2')

  td64.setAttribute("id", "EPS117-credits");
  var tr8 = document.createElement('tr');
  tr8.appendChild(th3);
  tr8.appendChild(td54);
  tr8.appendChild(td56);
  tr8.appendChild(td57);
  tr8.appendChild(td58);
  tr8.appendChild(td59);
  tr8.appendChild(td60);
  tr8.appendChild(td61);
  tr8.appendChild(td62);
  tr8.appendChild(td63);
  tr8.appendChild(td64); //Line 9

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EPS118-codeue");
  td45.innerHTML = "EPS118";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EPS118-matiere");
  td46.innerHTML = "Technique D'Expression Fran\xE7aise";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EPS118-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EPS118-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EPS118-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EPS118-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EPS118-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EPS118-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "EPS118-credits");
  var tr9 = document.createElement('tr');
  tr9.setAttribute('id', 'ligne-EPS118');
  tr9.appendChild(td45);
  tr9.appendChild(td46);
  tr9.appendChild(td47);
  tr9.appendChild(td48);
  tr9.appendChild(td49);
  tr9.appendChild(td50);
  tr9.appendChild(td51);
  tr9.appendChild(td52);
  tr9.appendChild(td53); //Line 10

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EPS119-codeue");
  td45.innerHTML = "EPS119";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EPS119-matiere");
  td46.innerHTML = "Technique D'Expression Anglaise. Anglaise- Forbi";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EPS119-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EPS119-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EPS119-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EPS119-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EPS119-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EPS119-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "EPS119-credits");
  var tr10 = document.createElement('tr');
  tr10.setAttribute('id', 'ligne-EPS119');
  tr10.appendChild(td45);
  tr10.appendChild(td46);
  tr10.appendChild(td47);
  tr10.appendChild(td48);
  tr10.appendChild(td49);
  tr10.appendChild(td50);
  tr10.appendChild(td51);
  tr10.appendChild(td52);
  tr10.appendChild(td53); //Line 11

  var td100 = document.createElement('td');
  td100.setAttribute('colspan', '4');
  td100.innerHTML = "RESULTATS SEMESTRE 1";
  var td101 = document.createElement('td');
  td101.setAttribute("id", "resultat-coef");
  var td102 = document.createElement('td');
  td102.setAttribute("id", "resultat-total");
  var td103 = document.createElement('td');
  td103.setAttribute("id", "resultat-moyenne");
  var td104 = document.createElement('td');
  td104.setAttribute("id", "resultat-rang");
  var td105 = document.createElement('td');
  td105.setAttribute("colspan", "2");
  td105.setAttribute("id", "resultat");
  td105.innerHTML = "Total Cr\xE9dits Semestre 1";
  var td106 = document.createElement('td');
  td106.setAttribute("id", "resultat-crédits");
  var tr11 = document.createElement('tr');
  tr11.setAttribute('id', 'ligne-13');
  tr11.appendChild(td100);
  tr11.appendChild(td101);
  tr11.appendChild(td102);
  tr11.appendChild(td103);
  tr11.appendChild(td104);
  tr11.appendChild(td105);
  tr11.appendChild(td106); //tbody

  var tbody = document.createElement('tbody');
  tbody.appendChild(tr2);
  tbody.appendChild(tr3);
  tbody.appendChild(tr4);
  tbody.appendChild(tr5);
  tbody.appendChild(tr6);
  tbody.appendChild(tr6a);
  tbody.appendChild(tr6b);
  tbody.appendChild(tr6j);
  tbody.appendChild(tr7);
  tbody.appendChild(tr8);
  tbody.appendChild(tr9);
  tbody.appendChild(tr10);
  tbody.appendChild(tr11);
  var table1 = document.createElement('table');
  table1.setAttribute('class', 'table-1');
  table1.appendChild(thead1);
  table1.appendChild(tbody); //table3
  //thead2

  var tr12 = document.createElement('tr');

  for (i = 0; i <= 11; i++) {
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');

    if (i == 0) {
      th.innerHTML = "&nbsp;&nbsp;";
    }

    tr12.appendChild(th);
  }

  var thead2 = document.createElement('thead');
  thead2.appendChild(tr12); //tbody
  //Line 1

  var tr13 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne de Classe de l'\xE9tudiant :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Maximum :";
    }

    if (i == 7) {
      td.innerHTML = "Retard :";
    }

    tr13.appendChild(td);
  } //Line 2


  var tr14 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne G\xE9n\xE9rale de la classe :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Minimum :";
    }

    if (i == 7) {
      td.innerHTML = "Absences:";
    }

    tr14.appendChild(td);
  } //Line 3


  var tr15 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
    }

    if (i == 4) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Rang :";
    }

    if (i == 5) {
      td.innerHTML = " sur ";
    }

    tr15.appendChild(td);
  } //Line 4


  var tbody3 = document.createElement('tbody');
  tbody3.setAttribute('id', 'tbody-3');
  tbody3.appendChild(tr13);
  tbody3.appendChild(tr14);
  tbody3.appendChild(tr15);
  var table3 = document.createElement('table');
  table3.setAttribute('id', 'table-3');
  table3.appendChild(thead2);
  table3.appendChild(tbody3); //semester Result

  var semestreResult = document.createElement('div');
  semestreResult.setAttribute('id', 'semester-result');
  semestreResult.appendChild(table1);
  semestreResult.appendChild(table3); //Main

  var main = document.createElement('main');
  main.appendChild(bullchecktitle);
  main.appendChild(infostudent);
  main.appendChild(semestreResult); //Footer

  var visa = document.createElement('div');
  visa.setAttribute('class', 'visa');
  visa.innerHTML = "VISA CHEF ETABLISSEMENT";
  var footer = document.createElement('footer');
  footer.appendChild(visa); //TEST

  containerbull = document.createElement('div');
  containerbull.setAttribute('class', 'container-bull');
  containerbull.appendChild(header);
  containerbull.appendChild(hr);
  containerbull.appendChild(main);
  containerbull.appendChild(footer); //TEST

  return containerbull;
}
/*DECLARATION S3 STAPS*/


function GenerateBullStaps2Semestre3() {
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
  var body = document.getElementsByTagName('body');
  body[0].appendChild(header);
  var hr = document.createElement('hr');
  var bullcheck = document.createElement('div');
  bullcheck.setAttribute('id', 'bull-check');
  bullcheck.innerHTML = "DAF/SG/DE/PR";
  var bulltitle = document.createElement('div');
  bulltitle.setAttribute('id', 'bull-title');
  bulltitle.innerHTML = "BULLETIN DE NOTES SEMESTRE 3";
  var bullchecktitle = document.createElement('div');
  bullchecktitle.setAttribute('id', 'bull-check-title');
  bullchecktitle.appendChild(bullcheck);
  bullchecktitle.appendChild(bulltitle); //info student

  var info1 = document.createElement('div');
  info1.setAttribute('class', 'info-student-style');
  info1.innerHTML = "Fili\xE8re &nbsp;&nbsp; : STAPS";
  var info2 = document.createElement('div');
  info2.setAttribute('class', 'info-student-style');
  info2.innerHTML = "Sp\xE9cialit\xE9 &nbsp;:  EPS";
  var info3 = document.createElement('div');
  info3.setAttribute('class', 'info-student-style');
  info3.innerHTML = "Nom (s) &nbsp; &nbsp; : ";
  var info4 = document.createElement('div');
  info4.setAttribute('class', 'info-student-style');
  info4.innerHTML = "Pr\xE9nom (s) : ";
  var info5 = document.createElement('div');
  info5.setAttribute('class', 'info-student-style');
  info5.innerHTML = "Nationalit\xE9 : Camerounais(e)";
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
  info111.innerHTML = "Niveau: II";
  var infostudent3 = document.createElement('div');
  infostudent3.setAttribute('id', 'info-student-3');
  infostudent3.appendChild(info111);
  var infostudent = document.createElement('div');
  infostudent.setAttribute('id', 'info-student');
  infostudent.appendChild(infostudent1);
  infostudent.appendChild(infostudent2);
  infostudent.appendChild(infostudent3); //table1
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
  th1.setAttribute('rowspan', '15');
  th1.innerHTML = "SEMESTRE 3";
  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '2');
  th2.innerHTML = "UE Fondamentales";
  var td1 = document.createElement('td');
  td1.setAttribute('id', 'EPS231-codeue');
  td1.innerHTML = "EPS231";
  var td2 = document.createElement('td');
  td2.setAttribute('id', 'EPS231-matiere');
  td2.innerHTML = "Education Physique : Loisirs";
  var td3 = document.createElement('td');
  td3.setAttribute('id', 'EPS231-note');
  var td4 = document.createElement('td');
  td4.setAttribute('id', 'EPS231-coef');
  var td5 = document.createElement('td');
  td5.setAttribute('id', 'EPS231-total');
  var td6 = document.createElement('td');
  td6.setAttribute('id', 'EPS231-moyenne');
  td6.setAttribute('rowspan', '2');
  var td7 = document.createElement('td');
  td7.setAttribute('id', 'EPS231-rang');
  var td8 = document.createElement('td');
  td8.setAttribute('id', 'EPS231-mention');
  var td9 = document.createElement('td');
  td9.setAttribute('id', 'EPS231-session');
  var td10 = document.createElement('td');
  td10.setAttribute('id', 'EPS231-credits');
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
  td11.setAttribute('id', 'EPS231-codeue');
  td11.innerHTML = "EPS232";
  var td12 = document.createElement('td');
  td12.setAttribute('id', 'EPS232-matiere');
  td12.innerHTML = "El\xE9ments de Psychop\xE9dagogie";
  var td13 = document.createElement('td');
  td13.setAttribute('id', 'EPS232-note');
  var td14 = document.createElement('td');
  td14.setAttribute('id', 'EPS232-coef');
  var td15 = document.createElement('td');
  td15.setAttribute('id', 'EPS232-total');
  var td16 = document.createElement('td');
  td16.setAttribute('id', 'EPS232-rang');
  var td17 = document.createElement('td');
  td17.setAttribute('id', 'EPS232-mention');
  var td18 = document.createElement('td');
  td18.setAttribute('id', 'EPS232-session');
  var td19 = document.createElement('td');
  td19.setAttribute('id', 'EPS232-credits');
  var tr3 = document.createElement('tr');
  tr3.appendChild(td11);
  tr3.appendChild(td12);
  tr3.appendChild(td13);
  tr3.appendChild(td14);
  tr3.appendChild(td15);
  tr3.appendChild(td16);
  tr3.appendChild(td17);
  tr3.appendChild(td18);
  tr3.appendChild(td19); //Line 4 //REGROUPER L4 et L5 dans une boucle

  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '9');
  th2.innerHTML = "UE Professionnelles";
  var td20 = document.createElement('td');
  td20.setAttribute("id", "EPS233-codeue");
  td20.innerHTML = "EPS233";
  var td21 = document.createElement('td');
  td21.setAttribute("id", "EPS233-matiere");
  td21.innerHTML = "Didactique De l'EPS III";
  var td22 = document.createElement('td');
  td22.setAttribute("id", "EPS233-note");
  var td222 = document.createElement('td');
  td222.setAttribute("id", "EPS233-coef");
  var td23 = document.createElement('td');
  td23.setAttribute("id", "EPS233-total");
  var td24 = document.createElement('td');
  td24.setAttribute("rowspan", "9");
  td24.setAttribute("id", "EPS233-moyenne");
  var td25 = document.createElement('td');
  td25.setAttribute("id", "EPS233-rang");
  var td26 = document.createElement('td');
  td26.setAttribute("id", "EPS233-mention");
  var td27 = document.createElement('td');
  td27.setAttribute("id", "EPS233-session");
  var td28 = document.createElement('td');
  td28.setAttribute("id", "EPS233-credits");
  var tr4 = document.createElement('tr');
  tr4.appendChild(th2);
  tr4.appendChild(td20);
  tr4.appendChild(td21);
  tr4.appendChild(td22);
  tr4.appendChild(td222);
  tr4.appendChild(td23);
  tr4.appendChild(td24);
  tr4.appendChild(td25);
  tr4.appendChild(td26);
  tr4.appendChild(td27);
  tr4.appendChild(td28); //Line 5

  var td28 = document.createElement('td');
  td28.setAttribute("id", "EPS234-codeue");
  td28.innerHTML = "EPS234";
  var td29 = document.createElement('td');
  td29.setAttribute("id", "EPS234-matiere");
  td29.innerHTML = "La Physiologie de L'Exercice II";
  var td30 = document.createElement('td');
  td30.setAttribute("id", "EPS234-note");
  var td31 = document.createElement('td');
  td31.setAttribute("id", "EPS234-coef");
  var td32 = document.createElement('td');
  td32.setAttribute("id", "EPS234-total");
  var td33 = document.createElement('td');
  td33.setAttribute("id", "EPS234-rang");
  var td34 = document.createElement('td');
  td34.setAttribute("id", "EPS234-mention");
  var td35 = document.createElement('td');
  td35.setAttribute("id", "EPS234-session");
  var td36 = document.createElement('td');
  td36.setAttribute("id", "EPS234-credits");
  var tr5 = document.createElement('tr');
  tr5.appendChild(td28);
  tr5.appendChild(td29);
  tr5.appendChild(td30);
  tr5.appendChild(td31);
  tr5.appendChild(td32);
  tr5.appendChild(td33);
  tr5.appendChild(td34);
  tr5.appendChild(td35);
  tr5.appendChild(td36); //Line 6a

  var td377a = document.createElement('td');
  td377a.setAttribute("id", "EPS235a-codeue");
  td377a.innerHTML = "EPS235";
  var td37a = document.createElement('td');
  td37a.setAttribute("id", "EPS235a-matiere");
  td37a.innerHTML = "Didactique Des APS: Athl\xE9tisme";
  var td38a = document.createElement('td');
  td38a.setAttribute("id", "EPS235a-note");
  var td39a = document.createElement('td');
  td39a.setAttribute("id", "EPS235a-coef");
  var td40a = document.createElement('td');
  td40a.setAttribute("id", "EPS235a-total");
  var td41a = document.createElement('td');
  td41a.setAttribute("id", "EPS235a-rang");
  var td42a = document.createElement('td');
  td42a.setAttribute("id", "EPS235a-mention");
  var td43a = document.createElement('td');
  td43a.setAttribute("id", "EPS235a-session");
  var td44a = document.createElement('td');
  td44a.setAttribute('rowspan', '6');
  td44a.setAttribute("id", "EPS235a-credits");
  var tr6a = document.createElement('tr');
  tr6a.appendChild(td377a);
  tr6a.appendChild(td37a);
  tr6a.appendChild(td38a);
  tr6a.appendChild(td39a);
  tr6a.appendChild(td40a);
  tr6a.appendChild(td41a);
  tr6a.appendChild(td42a);
  tr6a.appendChild(td43a);
  tr6a.appendChild(td44a); //Line 6b

  var td377b = document.createElement('td');
  td377b.setAttribute("id", "EPS235b-codeue");
  td377b.innerHTML = "EPS235";
  var td37b = document.createElement('td');
  td37b.setAttribute("id", "EPS235b-matiere");
  td37b.innerHTML = "Didactique Des APS: Basket Ball";
  var td38b = document.createElement('td');
  td38b.setAttribute("id", "EPS235b-note");
  var td39b = document.createElement('td');
  td39b.setAttribute("id", "EPS235b-coef");
  var td40b = document.createElement('td');
  td40b.setAttribute("id", "EPS235b-total");
  var td41b = document.createElement('td');
  td41b.setAttribute("id", "EPS235b-rang");
  var td42b = document.createElement('td');
  td42b.setAttribute("id", "EPS235b-mention");
  var td43b = document.createElement('td');
  td43b.setAttribute("id", "EPS235b-session");
  /*var td44b=document.createElement('td')
  td44b.setAttribute("id","EPS235b-credits")*/

  var tr6b = document.createElement('tr');
  tr6b.setAttribute('id', 'ligne-eps235b');
  tr6b.appendChild(td377b);
  tr6b.appendChild(td37b);
  tr6b.appendChild(td38b);
  tr6b.appendChild(td39b);
  tr6b.appendChild(td40b);
  tr6b.appendChild(td41b);
  tr6b.appendChild(td42b);
  tr6b.appendChild(td43b); //tr6b.appendChild(td44b)
  //Line 6f

  var td377f = document.createElement('td');
  td377f.setAttribute("id", "EPS235f-codeue");
  td377f.innerHTML = "EPS235";
  var td37f = document.createElement('td');
  td37f.setAttribute("id", "EPS235f-matiere");
  td37f.innerHTML = "Didactique Des APS: Football";
  var td38f = document.createElement('td');
  td38f.setAttribute("id", "EPS235f-note");
  var td39f = document.createElement('td');
  td39f.setAttribute("id", "EPS235f-coef");
  var td40f = document.createElement('td');
  td40f.setAttribute("id", "EPS235f-total");
  var td41f = document.createElement('td');
  td41f.setAttribute("id", "EPS235f-rang");
  var td42f = document.createElement('td');
  td42f.setAttribute("id", "EPS235f-mention");
  var td43f = document.createElement('td');
  td43f.setAttribute("id", "EPS235f-session");
  /*var td44f=document.createElement('td')
  td44f.setAttribute("id","EPS235f-credits")*/

  var tr6f = document.createElement('tr');
  tr6f.appendChild(td377f);
  tr6f.appendChild(td37f);
  tr6f.appendChild(td38f);
  tr6f.appendChild(td39f);
  tr6f.appendChild(td40f);
  tr6f.appendChild(td41f);
  tr6f.appendChild(td42f);
  tr6f.appendChild(td43f); //tr6f.appendChild(td44f)
  //Line 6g

  var td377g = document.createElement('td');
  td377g.setAttribute("id", "EPS235g-codeue");
  td377g.innerHTML = "EPS235";
  var td37g = document.createElement('td');
  td37g.setAttribute("id", "EPS235g-matiere");
  td37g.innerHTML = "Didactique Des APS: Gymnastique";
  var td38g = document.createElement('td');
  td38g.setAttribute("id", "EPS235g-note");
  var td39g = document.createElement('td');
  td39g.setAttribute("id", "EPS235g-coef");
  var td40g = document.createElement('td');
  td40g.setAttribute("id", "EPS235g-total");
  var td41g = document.createElement('td');
  td41g.setAttribute("id", "EPS235g-rang");
  var td42g = document.createElement('td');
  td42g.setAttribute("id", "EPS235g-mention");
  var td43g = document.createElement('td');
  td43g.setAttribute("id", "EPS235g-session");
  /*var td44g=document.createElement('td')
  td44g.setAttribute("id","EPS235g-credits")*/

  var tr6g = document.createElement('tr');
  tr6g.appendChild(td377g);
  tr6g.appendChild(td37g);
  tr6g.appendChild(td38g);
  tr6g.appendChild(td39g);
  tr6g.appendChild(td40g);
  tr6g.appendChild(td41g);
  tr6g.appendChild(td42g);
  tr6g.appendChild(td43g); //tr6g.appendChild(td44g)
  //Line 6j

  var td377j = document.createElement('td');
  td377j.setAttribute("id", "EPS235j-codeue");
  td377j.innerHTML = "EPS235";
  var td37j = document.createElement('td');
  td37j.setAttribute("id", "EPS235j-matiere");
  td37j.innerHTML = "Didactique Des APS: Judo";
  var td38j = document.createElement('td');
  td38j.setAttribute("id", "EPS235j-note");
  var td39j = document.createElement('td');
  td39j.setAttribute("id", "EPS235j-coef");
  var td40j = document.createElement('td');
  td40j.setAttribute("id", "EPS235j-total");
  var td41j = document.createElement('td');
  td41j.setAttribute("id", "EPS235j-rang");
  var td42j = document.createElement('td');
  td42j.setAttribute("id", "EPS235j-mention");
  var td43j = document.createElement('td');
  td43j.setAttribute("id", "EPS235j-session");
  /*var td44j=document.createElement('td')
  td44j.setAttribute("id","EPS235j-credits")*/

  var tr6j = document.createElement('tr');
  tr6j.setAttribute('id', 'ligne-eps235j');
  tr6j.appendChild(td377j);
  tr6j.appendChild(td37j);
  tr6j.appendChild(td38j);
  tr6j.appendChild(td39j);
  tr6j.appendChild(td40j);
  tr6j.appendChild(td41j);
  tr6j.appendChild(td42j);
  tr6j.appendChild(td43j); //tr6j.appendChild(td44j)
  //Line 6j

  var td377l = document.createElement('td');
  td377l.setAttribute("id", "EPS235l-codeue");
  td377l.innerHTML = "EPS235";
  var td37l = document.createElement('td');
  td37l.setAttribute("id", "EPS235l-matiere");
  td37l.innerHTML = "Didactique Des APS: Lutte";
  var td38l = document.createElement('td');
  td38l.setAttribute("id", "EPS235l-note");
  var td39l = document.createElement('td');
  td39l.setAttribute("id", "EPS235l-coef");
  var td40l = document.createElement('td');
  td40l.setAttribute("id", "EPS235l-total");
  var td41l = document.createElement('td');
  td41l.setAttribute("id", "EPS235l-rang");
  var td42l = document.createElement('td');
  td42l.setAttribute("id", "EPS235l-mention");
  var td43l = document.createElement('td');
  td43l.setAttribute("id", "EPS235l-session");
  /*var td44l=document.createElement('td')
  td44l.setAttribute("id","EPS235l-credits")*/

  var tr6l = document.createElement('tr');
  tr6l.setAttribute('id', 'ligne-eps235l');
  tr6l.appendChild(td377l);
  tr6l.appendChild(td37l);
  tr6l.appendChild(td38l);
  tr6l.appendChild(td39l);
  tr6l.appendChild(td40l);
  tr6l.appendChild(td41l);
  tr6l.appendChild(td42l);
  tr6l.appendChild(td43l); //tr6l.appendChild(td44l)
  //Line 7

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EPS236-codeue");
  td45.innerHTML = "EPS236";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EPS236-matiere");
  td46.innerHTML = "P\xE9dagogie Pratique II";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EPS236-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EPS236-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EPS236-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EPS236-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EPS236-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EPS236-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "EPS236-credits");
  var tr7 = document.createElement('tr');
  tr7.setAttribute('id', 'ligne-eps236');
  tr7.appendChild(td45);
  tr7.appendChild(td46);
  tr7.appendChild(td47);
  tr7.appendChild(td48);
  tr7.appendChild(td49);
  tr7.appendChild(td50);
  tr7.appendChild(td51);
  tr7.appendChild(td52);
  tr7.appendChild(td53); //Line 8

  var th3 = document.createElement('th');
  th3.setAttribute('scope', 'row');
  th3.setAttribute('rowspan', '3');
  th3.innerHTML = "UE Transversales";
  var td54 = document.createElement('td');
  td54.setAttribute("id", "EPS237-codeue");
  td54.innerHTML = "EPS237";
  var td56 = document.createElement('td');
  td56.setAttribute("id", "EPS237-matiere");
  td56.innerHTML = "Formation Bilingue -Anglais appliqu\xE9 au APS";
  var td57 = document.createElement('td');
  td57.setAttribute("id", "EPS237-note");
  var td58 = document.createElement('td');
  td58.setAttribute("id", "EPS237-coef");
  var td59 = document.createElement('td');
  td59.setAttribute("id", "EPS237-total");
  var td60 = document.createElement('td');
  td60.setAttribute("rowspan", "3");
  td60.setAttribute("id", "EPS237-moyenne");
  var td61 = document.createElement('td');
  td61.setAttribute("id", "EPS237-rang");
  var td62 = document.createElement('td');
  td62.setAttribute("id", "EPS237-mention");
  var td63 = document.createElement('td');
  td63.setAttribute("id", "EPS237-session");
  var td64 = document.createElement('td'); //td64.setAttribute('rowspan','3')

  td64.setAttribute("id", "EPS237-credits");
  var tr8 = document.createElement('tr');
  tr8.appendChild(th3);
  tr8.appendChild(td54);
  tr8.appendChild(td56);
  tr8.appendChild(td57);
  tr8.appendChild(td58);
  tr8.appendChild(td59);
  tr8.appendChild(td60);
  tr8.appendChild(td61);
  tr8.appendChild(td62);
  tr8.appendChild(td63);
  tr8.appendChild(td64); //Line 9

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EPS238-codeue");
  td45.innerHTML = "EPS238";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EPS238-matiere");
  td46.innerHTML = "Technique D'Expression Fran\xE7aise";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EPS238-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EPS238-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EPS238-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EPS238-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EPS238-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EPS238-session");
  var td53 = document.createElement('td');
  td53.setAttribute('rowspan', '2');
  td53.setAttribute("id", "EPS238-credits");
  var tr9 = document.createElement('tr');
  tr9.appendChild(td45);
  tr9.appendChild(td46);
  tr9.appendChild(td47);
  tr9.appendChild(td48);
  tr9.appendChild(td49);
  tr9.appendChild(td50);
  tr9.appendChild(td51);
  tr9.appendChild(td52);
  tr9.appendChild(td53); //Line 10

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EPS239-codeue");
  td45.innerHTML = "EPS239";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EPS239-matiere");
  td46.innerHTML = "Informatique";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EPS239-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EPS239-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EPS239-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EPS239-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EPS239-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EPS239-session");
  /*var td53=document.createElement('td')
  td53.setAttribute("id","EPS239-credits")*/

  var tr10 = document.createElement('tr');
  tr10.appendChild(td45);
  tr10.appendChild(td46);
  tr10.appendChild(td47);
  tr10.appendChild(td48);
  tr10.appendChild(td49);
  tr10.appendChild(td50);
  tr10.appendChild(td51);
  tr10.appendChild(td52); //tr10.appendChild(td53)
  //Line 11

  var td100 = document.createElement('td');
  td100.setAttribute('colspan', '4');
  td100.innerHTML = "RESULTATS SEMESTRE 3";
  var td101 = document.createElement('td');
  td101.setAttribute("id", "resultat-coef");
  var td102 = document.createElement('td');
  td102.setAttribute("id", "resultat-total");
  var td103 = document.createElement('td');
  td103.setAttribute("id", "resultat-moyenne");
  var td104 = document.createElement('td');
  td104.setAttribute("id", "resultat-rang");
  var td105 = document.createElement('td');
  td105.setAttribute("colspan", "2");
  td105.setAttribute("id", "resultat");
  td105.innerHTML = "Total Cr\xE9dits Semestre 3";
  var td106 = document.createElement('td');
  td106.setAttribute("id", "resultat-crédits");
  var tr11 = document.createElement('tr');
  tr11.setAttribute('id', 'resultat-eps2');
  tr11.appendChild(td100);
  tr11.appendChild(td101);
  tr11.appendChild(td102);
  tr11.appendChild(td103);
  tr11.appendChild(td104);
  tr11.appendChild(td105);
  tr11.appendChild(td106); //tbody

  var tbody = document.createElement('tbody');
  tbody.appendChild(tr2);
  tbody.appendChild(tr3);
  tbody.appendChild(tr4);
  tbody.appendChild(tr5);
  tbody.appendChild(tr6a);
  tbody.appendChild(tr6b);
  tbody.appendChild(tr6f);
  tbody.appendChild(tr6g);
  tbody.appendChild(tr6j);
  tbody.appendChild(tr6l);
  tbody.appendChild(tr7);
  tbody.appendChild(tr8);
  tbody.appendChild(tr9);
  tbody.appendChild(tr10);
  tbody.appendChild(tr11);
  table1 = document.createElement('table');
  table1.setAttribute('class', 'table-1');
  table1.appendChild(thead1);
  table1.appendChild(tbody); //table3
  //thead2

  var tr12 = document.createElement('tr');

  for (i = 0; i <= 11; i++) {
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');

    if (i == 0) {
      th.innerHTML = "&nbsp;&nbsp;";
    }

    tr12.appendChild(th);
  }

  var thead2 = document.createElement('thead');
  thead2.appendChild(tr12); //tbody
  //Line 1

  var tr13 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne de Classe de l'\xE9tudiant :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Maximum :";
    }

    if (i == 7) {
      td.innerHTML = "Retard :";
    }

    tr13.appendChild(td);
  } //Line 2


  var tr14 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne G\xE9n\xE9rale de la classe :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Minimum :";
    }

    if (i == 7) {
      td.innerHTML = "Absences:";
    }

    tr14.appendChild(td);
  } //Line 3


  var tr15 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
    }

    if (i == 4) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Rang :";
    } //if(i==8){td.innerHTML=`Absences:`}


    if (i == 5) {
      td.innerHTML = " sur ";
    }

    tr15.appendChild(td);
  } //Line 4


  var tbody3 = document.createElement('tbody');
  tbody3.setAttribute('id', 'tbody-3');
  tbody3.appendChild(tr13);
  tbody3.appendChild(tr14);
  tbody3.appendChild(tr15);
  var table3 = document.createElement('table');
  table3.setAttribute('id', 'table-3');
  table3.appendChild(thead2);
  table3.appendChild(tbody3); //semester Result

  var semestreResult = document.createElement('div');
  semestreResult.setAttribute('id', 'semester-result');
  semestreResult.appendChild(table1);
  semestreResult.appendChild(table3); //Main

  var main = document.createElement('main');
  main.appendChild(bullchecktitle);
  main.appendChild(infostudent);
  main.appendChild(semestreResult); //Footer

  var visa = document.createElement('div');
  visa.setAttribute('class', 'visa');
  visa.innerHTML = "VISA CHEF ETABLISSEMENT";
  var footer = document.createElement('footer');
  footer.appendChild(visa); //TEST

  containerbull = document.createElement('div');
  containerbull.setAttribute('class', 'container-bull');
  containerbull.appendChild(header);
  containerbull.appendChild(hr);
  containerbull.appendChild(main);
  containerbull.appendChild(footer); //TEST

  /*body=document.getElementsByTagName('body')
  body[0].appendChild(containerbull)*/

  return containerbull;
}
/*DECLARATION SEMESTRE 5 EVE */


function GenerateBullEVEsemestre5() {
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
  var bullcheck = document.createElement('div');
  bullcheck.setAttribute('id', 'bull-check');
  bullcheck.innerHTML = "DAF/SG/DE/PR";
  var bulltitle = document.createElement('div');
  bulltitle.setAttribute('id', 'bull-title');
  bulltitle.innerHTML = "BULLETIN DE NOTES SEMESTRE 5";
  var bullchecktitle = document.createElement('div');
  bullchecktitle.setAttribute('id', 'bull-check-title');
  bullchecktitle.appendChild(bullcheck);
  bullchecktitle.appendChild(bulltitle); //info student

  var info1 = document.createElement('div');
  info1.setAttribute('class', 'info-student-style');
  info1.innerHTML = "Fili\xE8re &nbsp;&nbsp; : MAS";
  var info2 = document.createElement('div');
  info2.setAttribute('class', 'info-student-style');
  info2.innerHTML = "Sp\xE9cialit\xE9 &nbsp;:  EVE";
  var info3 = document.createElement('div');
  info3.setAttribute('class', 'info-student-style');
  info3.innerHTML = "Nom (s) &nbsp; &nbsp; : ";
  var info4 = document.createElement('div');
  info4.setAttribute('class', 'info-student-style');
  info4.innerHTML = "Pr\xE9nom (s) : ";
  var info5 = document.createElement('div');
  info5.setAttribute('class', 'info-student-style');
  info5.innerHTML = "Nationalit\xE9 : Camerounais(e)";
  var infostudent1 = document.createElement('div');
  infostudent1.setAttribute('id', 'info-student-1');
  infostudent1.appendChild(info1);
  infostudent1.appendChild(info2);
  infostudent1.appendChild(info3);
  infostudent1.appendChild(info4);
  infostudent1.appendChild(info5);
  var info11 = document.createElement('div');
  info11.setAttribute('class', 'info-student-style');
  info11.innerHTML = "Grade : LICENCE ";
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
  info111.innerHTML = "Niveau: III";
  var infostudent3 = document.createElement('div');
  infostudent3.setAttribute('id', 'info-student-3');
  infostudent3.appendChild(info111);
  var infostudent = document.createElement('div');
  infostudent.setAttribute('id', 'info-student');
  infostudent.appendChild(infostudent1);
  infostudent.appendChild(infostudent2);
  infostudent.appendChild(infostudent3); //table1
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
  th1.setAttribute('rowspan', '7');
  th1.innerHTML = "SEMESTRE 5";
  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '4');
  th2.innerHTML = "UE Fondamentales";
  var td1 = document.createElement('td');
  td1.setAttribute('id', 'MAS315-codeue');
  td1.innerHTML = "MAS315";
  var td2 = document.createElement('td');
  td2.setAttribute('id', 'MAS315-matiere');
  td2.innerHTML = "Environnement Institutionnel De la pratique du Sport";
  var td3 = document.createElement('td');
  td3.setAttribute('id', 'MAS315-note');
  var td4 = document.createElement('td');
  td4.setAttribute('id', 'MAS315-coef');
  var td5 = document.createElement('td');
  td5.setAttribute('id', 'MAS315-total');
  var td6 = document.createElement('td');
  td6.setAttribute('id', 'MAS315-moyenne');
  td6.setAttribute('rowspan', '4');
  var td7 = document.createElement('td');
  td7.setAttribute('id', 'MAS315-rang');
  var td8 = document.createElement('td');
  td8.setAttribute('id', 'MAS315-mention');
  var td9 = document.createElement('td');
  td9.setAttribute('id', 'MAS315-session');
  var td10 = document.createElement('td');
  td10.setAttribute('id', 'MAS315-credits');
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
  td11.setAttribute('id', 'MAS325-codeue');
  td11.innerHTML = "MAS325";
  var td12 = document.createElement('td');
  td12.setAttribute('id', 'MAS325-matiere');
  td12.innerHTML = "Montage Des Projets Et Entrepreneuriat Sportif";
  var td13 = document.createElement('td');
  td13.setAttribute('id', 'MAS325-note');
  var td14 = document.createElement('td');
  td14.setAttribute('id', 'MAS325-coef');
  var td15 = document.createElement('td');
  td15.setAttribute('id', 'MAS325-total');
  var td16 = document.createElement('td');
  td16.setAttribute('id', 'MAS325-rang');
  var td17 = document.createElement('td');
  td17.setAttribute('id', 'MAS325-mention');
  var td18 = document.createElement('td');
  td18.setAttribute('id', 'MAS325-session');
  var td19 = document.createElement('td');
  td19.setAttribute('id', 'EPS325-credits');
  var tr3 = document.createElement('tr');
  tr3.appendChild(td11);
  tr3.appendChild(td12);
  tr3.appendChild(td13);
  tr3.appendChild(td14);
  tr3.appendChild(td15);
  tr3.appendChild(td16);
  tr3.appendChild(td17);
  tr3.appendChild(td18);
  tr3.appendChild(td19);
  var td20 = document.createElement('td');
  td20.setAttribute("id", "MAS335-codeue");
  td20.innerHTML = "MAS335";
  var td21 = document.createElement('td');
  td21.setAttribute("id", "MAS335-matiere");
  td21.innerHTML = "Information Et Communication Strat\xE9giques dans le Sport et les Loisirs";
  var td22 = document.createElement('td');
  td22.setAttribute("id", "MAS335-note");
  var td222 = document.createElement('td');
  td222.setAttribute("id", "MAS335-coef");
  var td23 = document.createElement('td');
  td23.setAttribute("id", "MAS335-total");
  var td25 = document.createElement('td');
  td25.setAttribute("id", "MAS335-rang");
  var td26 = document.createElement('td');
  td26.setAttribute("id", "MAS335-mention");
  var td27 = document.createElement('td');
  td27.setAttribute("id", "MAS335-session");
  var td28 = document.createElement('td');
  td28.setAttribute("id", "MAS335-credits");
  var tr4 = document.createElement('tr');
  tr4.appendChild(td20);
  tr4.appendChild(td21);
  tr4.appendChild(td22);
  tr4.appendChild(td222);
  tr4.appendChild(td23);
  tr4.appendChild(td25);
  tr4.appendChild(td26);
  tr4.appendChild(td27);
  tr4.appendChild(td28); //Line 5

  var td28 = document.createElement('td');
  td28.setAttribute("id", "MAS345-codeue");
  td28.innerHTML = "MAS345";
  var td29 = document.createElement('td');
  td29.setAttribute("id", "MAS345-matiere");
  td29.innerHTML = "E-sport";
  var td30 = document.createElement('td');
  td30.setAttribute("id", "MAS345-note");
  var td31 = document.createElement('td');
  td31.setAttribute("id", "MAS345-coef");
  var td32 = document.createElement('td');
  td32.setAttribute("id", "MAS345-total");
  var td33 = document.createElement('td');
  td33.setAttribute("id", "MAS345-rang");
  var td34 = document.createElement('td');
  td34.setAttribute("id", "MAS345-mention");
  var td35 = document.createElement('td');
  td35.setAttribute("id", "MAS345-session");
  var td36 = document.createElement('td');
  td36.setAttribute("id", "MAS345-credits");
  var tr5 = document.createElement('tr');
  tr5.appendChild(td28);
  tr5.appendChild(td29);
  tr5.appendChild(td30);
  tr5.appendChild(td31);
  tr5.appendChild(td32);
  tr5.appendChild(td33);
  tr5.appendChild(td34);
  tr5.appendChild(td35);
  tr5.appendChild(td36); //Line 8

  var th3 = document.createElement('th');
  th3.setAttribute('scope', 'row');
  th3.setAttribute('rowspan', '2');
  th3.innerHTML = "UE Sp\xE9cialit\xE9";
  var td54 = document.createElement('td');
  td54.setAttribute("id", "EVE355-codeue");
  td54.innerHTML = "EVE355";
  var td56 = document.createElement('td');
  td56.setAttribute("id", "EVE355-matiere");
  td56.innerHTML = "Multim\xE9dias dans le D\xE9veloppement Du Sport et Des Loisirs";
  var td57 = document.createElement('td');
  td57.setAttribute("id", "EVE355-note");
  var td58 = document.createElement('td');
  td58.setAttribute("id", "EVE355-coef");
  var td59 = document.createElement('td');
  td59.setAttribute("id", "EVE355-total");
  var td60 = document.createElement('td');
  td60.setAttribute("rowspan", "2");
  td60.setAttribute("id", "EVE355-moyenne");
  var td61 = document.createElement('td');
  td61.setAttribute("id", "EVE355-rang");
  var td62 = document.createElement('td');
  td62.setAttribute("id", "EVE355-mention");
  var td63 = document.createElement('td');
  td63.setAttribute("id", "EVE355-session");
  var td64 = document.createElement('td');
  td64.setAttribute("id", "EVE355-credits");
  var tr8 = document.createElement('tr');
  tr8.appendChild(th3);
  tr8.appendChild(td54);
  tr8.appendChild(td56);
  tr8.appendChild(td57);
  tr8.appendChild(td58);
  tr8.appendChild(td59);
  tr8.appendChild(td60);
  tr8.appendChild(td61);
  tr8.appendChild(td62);
  tr8.appendChild(td63);
  tr8.appendChild(td64); //Line 9

  var td45 = document.createElement('td');
  td45.setAttribute("id", "EVE365-codeue");
  td45.innerHTML = "EVE365";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "EVE365-matiere");
  td46.innerHTML = "Ing\xE9nierie De L'Animation Sportive Et Culturelle";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "EVE365-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "EVE365-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "EVE365-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "EVE365-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "EVE365-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "EVE365-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "EVE365-credits");
  var tr9 = document.createElement('tr');
  tr9.appendChild(td45);
  tr9.appendChild(td46);
  tr9.appendChild(td47);
  tr9.appendChild(td48);
  tr9.appendChild(td49);
  tr9.appendChild(td50);
  tr9.appendChild(td51);
  tr9.appendChild(td52);
  tr9.appendChild(td53); //Line 11

  var td100 = document.createElement('td');
  td100.setAttribute('colspan', '4');
  td100.innerHTML = "RESULTATS SEMESTRE 1";
  var td101 = document.createElement('td');
  td101.setAttribute("id", "resultat-coef");
  var td102 = document.createElement('td');
  td102.setAttribute("id", "resultat-total");
  var td103 = document.createElement('td');
  td103.setAttribute("id", "resultat-moyenne");
  var td104 = document.createElement('td');
  td104.setAttribute("id", "resultat-rang");
  var td105 = document.createElement('td');
  td105.setAttribute("colspan", "2");
  td105.setAttribute("id", "resultat");
  td105.innerHTML = "Total Cr\xE9dits Semestre 1";
  var td106 = document.createElement('td');
  td106.setAttribute("id", "resultat-crédits");
  var tr11 = document.createElement('tr');
  tr11.appendChild(td100);
  tr11.appendChild(td101);
  tr11.appendChild(td102);
  tr11.appendChild(td103);
  tr11.appendChild(td104);
  tr11.appendChild(td105);
  tr11.appendChild(td106); //tbody

  var tbody = document.createElement('tbody');
  tbody.setAttribute('id', 'tbody01');
  tbody.appendChild(tr2);
  tbody.appendChild(tr3);
  tbody.appendChild(tr4);
  tbody.appendChild(tr5);
  tbody.appendChild(tr8);
  tbody.appendChild(tr9);
  tbody.appendChild(tr11);
  var table1 = document.createElement('table');
  table1.setAttribute('class', 'table-1');
  table1.appendChild(thead1);
  table1.appendChild(tbody); //table3
  //thead2

  var tr12 = document.createElement('tr');

  for (i = 0; i <= 11; i++) {
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');

    if (i == 0) {
      th.innerHTML = "&nbsp;&nbsp;";
    }

    tr12.appendChild(th);
  }

  var thead2 = document.createElement('thead');
  thead2.appendChild(tr12); //tbody
  //Line 1

  var tr13 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne de Classe de l'\xE9tudiant :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Maximum :";
    }

    if (i == 7) {
      td.innerHTML = "Retard :";
    }

    tr13.appendChild(td);
  } //Line 2


  var tr14 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne G\xE9n\xE9rale de la classe :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Minimum :";
    }

    if (i == 7) {
      td.innerHTML = "Absences:";
    }

    tr14.appendChild(td);
  } //Line 3


  var tr15 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
    }

    if (i == 4) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Rang :";
    }

    if (i == 5) {
      td.innerHTML = " sur ";
    }

    tr15.appendChild(td);
  } //Line 4


  var tbody3 = document.createElement('tbody');
  tbody3.setAttribute('id', 'tbody-3');
  tbody3.appendChild(tr13);
  tbody3.appendChild(tr14);
  tbody3.appendChild(tr15);
  var table3 = document.createElement('table');
  table3.setAttribute('id', 'table-3');
  table3.appendChild(thead2);
  table3.appendChild(tbody3);
  var semestreResult = document.createElement('div');
  semestreResult.setAttribute('id', 'semester-result');
  semestreResult.appendChild(table1);
  semestreResult.appendChild(table3);
  var main = document.createElement('main');
  main.appendChild(bullchecktitle);
  main.appendChild(infostudent);
  main.appendChild(semestreResult);
  var visa = document.createElement('div');
  visa.setAttribute('class', 'visa');
  visa.innerHTML = "VISA CHEF ETABLISSEMENT";
  var footer = document.createElement('footer');
  footer.appendChild(visa);
  containerbull = document.createElement('div');
  containerbull.setAttribute('class', 'container-bull');
  containerbull.appendChild(header);
  containerbull.appendChild(hr);
  containerbull.appendChild(main);
  containerbull.appendChild(footer);
  /*body=document.getElementsByTagName('body')
  body[0].appendChild(containerbull)*/

  return containerbull;
}
/*DECLARATION GENERATION SEEMESTRE 5 MSO */


function GenerateBullMSOsemestre5() {
  var br = document.createElement('br');
  var slogan = document.createElement('div');
  slogan.innerHTML = "ARRETE N022-0003/L/MINESUP/DDES/ESUP/SDA/ABC";
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
  var bullcheck = document.createElement('div');
  bullcheck.setAttribute('id', 'bull-check');
  bullcheck.innerHTML = "DAF/SG/DE/PR";
  var bulltitle = document.createElement('div');
  bulltitle.setAttribute('id', 'bull-title');
  bulltitle.innerHTML = "BULLETIN DE NOTES SEMESTRE 5";
  var bullchecktitle = document.createElement('div');
  bullchecktitle.setAttribute('id', 'bull-check-title');
  bullchecktitle.appendChild(bullcheck);
  bullchecktitle.appendChild(bulltitle); //info student

  var info1 = document.createElement('div');
  info1.setAttribute('class', 'info-student-style');
  info1.innerHTML = "Fili\xE8re &nbsp;&nbsp; : MAS";
  var info2 = document.createElement('div');
  info2.setAttribute('class', 'info-student-style');
  info2.innerHTML = "Sp\xE9cialit\xE9 &nbsp;:  MSO";
  var info3 = document.createElement('div');
  info3.setAttribute('class', 'info-student-style');
  info3.innerHTML = "Nom (s) &nbsp; &nbsp; : ";
  var info4 = document.createElement('div');
  info4.setAttribute('class', 'info-student-style');
  info4.innerHTML = "Pr\xE9nom (s) : ";
  var info5 = document.createElement('div');
  info5.setAttribute('class', 'info-student-style');
  info5.innerHTML = "Nationalit\xE9 : Camerounais(e)";
  var infostudent1 = document.createElement('div');
  infostudent1.setAttribute('id', 'info-student-1');
  infostudent1.appendChild(info1);
  infostudent1.appendChild(info2);
  infostudent1.appendChild(info3);
  infostudent1.appendChild(info4);
  infostudent1.appendChild(info5);
  var info11 = document.createElement('div');
  info11.setAttribute('class', 'info-student-style');
  info11.innerHTML = "Grade : LICENCE ";
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
  info111.innerHTML = "Niveau: III";
  var infostudent3 = document.createElement('div');
  infostudent3.setAttribute('id', 'info-student-3');
  infostudent3.appendChild(info111);
  var infostudent = document.createElement('div');
  infostudent.setAttribute('id', 'info-student');
  infostudent.appendChild(infostudent1);
  infostudent.appendChild(infostudent2);
  infostudent.appendChild(infostudent3); //table1
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
  th1.setAttribute('rowspan', '7');
  th1.innerHTML = "SEMESTRE 5";
  var th2 = document.createElement('th');
  th2.setAttribute('scope', 'row');
  th2.setAttribute('rowspan', '4');
  th2.innerHTML = "UE Fondamentales";
  var td1 = document.createElement('td');
  td1.setAttribute('id', 'MAS315-codeue');
  td1.innerHTML = "MAS315";
  var td2 = document.createElement('td');
  td2.setAttribute('id', 'MAS315-matiere');
  td2.innerHTML = "Environnement Institutionnel De la pratique du Sport";
  var td3 = document.createElement('td');
  td3.setAttribute('id', 'MAS315-note');
  var td4 = document.createElement('td');
  td4.setAttribute('id', 'MAS315-coef');
  var td5 = document.createElement('td');
  td5.setAttribute('id', 'MAS315-total');
  var td6 = document.createElement('td');
  td6.setAttribute('id', 'MAS315-moyenne');
  td6.setAttribute('rowspan', '4');
  var td7 = document.createElement('td');
  td7.setAttribute('id', 'MAS315-rang');
  var td8 = document.createElement('td');
  td8.setAttribute('id', 'MAS315-mention');
  var td9 = document.createElement('td');
  td9.setAttribute('id', 'MAS315-session');
  var td10 = document.createElement('td');
  td10.setAttribute('id', 'MAS315-credits');
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
  td11.setAttribute('id', 'MAS325-codeue');
  td11.innerHTML = "MAS325";
  var td12 = document.createElement('td');
  td12.setAttribute('id', 'MAS325-matiere');
  td12.innerHTML = "Montage Des Projets Et Entrepreneuriat Sportif";
  var td13 = document.createElement('td');
  td13.setAttribute('id', 'MAS325-note');
  var td14 = document.createElement('td');
  td14.setAttribute('id', 'MAS325-coef');
  var td15 = document.createElement('td');
  td15.setAttribute('id', 'MAS325-total');
  var td16 = document.createElement('td');
  td16.setAttribute('id', 'MAS325-rang');
  var td17 = document.createElement('td');
  td17.setAttribute('id', 'MAS325-mention');
  var td18 = document.createElement('td');
  td18.setAttribute('id', 'MAS325-session');
  var td19 = document.createElement('td');
  td19.setAttribute('id', 'EPS325-credits');
  var tr3 = document.createElement('tr');
  tr3.appendChild(td11);
  tr3.appendChild(td12);
  tr3.appendChild(td13);
  tr3.appendChild(td14);
  tr3.appendChild(td15);
  tr3.appendChild(td16);
  tr3.appendChild(td17);
  tr3.appendChild(td18);
  tr3.appendChild(td19);
  var td20 = document.createElement('td');
  td20.setAttribute("id", "MAS335-codeue");
  td20.innerHTML = "MAS335";
  var td21 = document.createElement('td');
  td21.setAttribute("id", "MAS335-matiere");
  td21.innerHTML = "Information Et Communication Strat\xE9giques dans le Sport et les Loisirs";
  var td22 = document.createElement('td');
  td22.setAttribute("id", "MAS335-note");
  var td222 = document.createElement('td');
  td222.setAttribute("id", "MAS335-coef");
  var td23 = document.createElement('td');
  td23.setAttribute("id", "MAS335-total");
  var td25 = document.createElement('td');
  td25.setAttribute("id", "MAS335-rang");
  var td26 = document.createElement('td');
  td26.setAttribute("id", "MAS335-mention");
  var td27 = document.createElement('td');
  td27.setAttribute("id", "MAS335-session");
  var td28 = document.createElement('td');
  td28.setAttribute("id", "MAS335-credits");
  var tr4 = document.createElement('tr');
  tr4.appendChild(td20);
  tr4.appendChild(td21);
  tr4.appendChild(td22);
  tr4.appendChild(td222);
  tr4.appendChild(td23);
  tr4.appendChild(td25);
  tr4.appendChild(td26);
  tr4.appendChild(td27);
  tr4.appendChild(td28); //Line 5

  var td28 = document.createElement('td');
  td28.setAttribute("id", "MAS345-codeue");
  td28.innerHTML = "MAS345";
  var td29 = document.createElement('td');
  td29.setAttribute("id", "MAS345-matiere");
  td29.innerHTML = "E-sport";
  var td30 = document.createElement('td');
  td30.setAttribute("id", "MAS345-note");
  var td31 = document.createElement('td');
  td31.setAttribute("id", "MAS345-coef");
  var td32 = document.createElement('td');
  td32.setAttribute("id", "MAS345-total");
  var td33 = document.createElement('td');
  td33.setAttribute("id", "MAS345-rang");
  var td34 = document.createElement('td');
  td34.setAttribute("id", "MAS345-mention");
  var td35 = document.createElement('td');
  td35.setAttribute("id", "MAS345-session");
  var td36 = document.createElement('td');
  td36.setAttribute("id", "MAS345-credits");
  var tr5 = document.createElement('tr');
  tr5.appendChild(td28);
  tr5.appendChild(td29);
  tr5.appendChild(td30);
  tr5.appendChild(td31);
  tr5.appendChild(td32);
  tr5.appendChild(td33);
  tr5.appendChild(td34);
  tr5.appendChild(td35);
  tr5.appendChild(td36); //Line 8

  var th3 = document.createElement('th');
  th3.setAttribute('scope', 'row');
  th3.setAttribute('rowspan', '2');
  th3.innerHTML = "UE Sp\xE9cialit\xE9";
  var td54 = document.createElement('td');
  td54.setAttribute("id", "MSO355-codeue");
  td54.innerHTML = "MSO355";
  var td56 = document.createElement('td');
  td56.setAttribute("id", "MSO355-matiere");
  td56.innerHTML = "Ethique Sportive Et Programmes Olympiques";
  var td57 = document.createElement('td');
  td57.setAttribute("id", "MSO355-note");
  var td58 = document.createElement('td');
  td58.setAttribute("id", "MSO355-coef");
  var td59 = document.createElement('td');
  td59.setAttribute("id", "MSO355-total");
  var td60 = document.createElement('td');
  td60.setAttribute("rowspan", "2");
  td60.setAttribute("id", "MSO355-moyenne");
  var td61 = document.createElement('td');
  td61.setAttribute("id", "MSO355-rang");
  var td62 = document.createElement('td');
  td62.setAttribute("id", "MSO355-mention");
  var td63 = document.createElement('td');
  td63.setAttribute("id", "MSO355-session");
  var td64 = document.createElement('td');
  td64.setAttribute("id", "MSO355-credits");
  var tr8 = document.createElement('tr');
  tr8.appendChild(th3);
  tr8.appendChild(td54);
  tr8.appendChild(td56);
  tr8.appendChild(td57);
  tr8.appendChild(td58);
  tr8.appendChild(td59);
  tr8.appendChild(td60);
  tr8.appendChild(td61);
  tr8.appendChild(td62);
  tr8.appendChild(td63);
  tr8.appendChild(td64); //Line 9

  var td45 = document.createElement('td');
  td45.setAttribute("id", "MSO365-codeue");
  td45.innerHTML = "MSO365";
  var td46 = document.createElement('td');
  td46.setAttribute("id", "MSO365-matiere");
  td46.innerHTML = "Psychologie Du Travail Et des Organisations";
  var td47 = document.createElement('td');
  td47.setAttribute("id", "MSO365-note");
  var td48 = document.createElement('td');
  td48.setAttribute("id", "MSO365-coef");
  var td49 = document.createElement('td');
  td49.setAttribute("id", "MSO365-total");
  var td50 = document.createElement('td');
  td50.setAttribute("id", "MSO365-rang");
  var td51 = document.createElement('td');
  td51.setAttribute("id", "MSO365-mention");
  var td52 = document.createElement('td');
  td52.setAttribute("id", "MSO365-session");
  var td53 = document.createElement('td');
  td53.setAttribute("id", "MSO365-credits");
  var tr9 = document.createElement('tr');
  tr9.appendChild(td45);
  tr9.appendChild(td46);
  tr9.appendChild(td47);
  tr9.appendChild(td48);
  tr9.appendChild(td49);
  tr9.appendChild(td50);
  tr9.appendChild(td51);
  tr9.appendChild(td52);
  tr9.appendChild(td53); //Line 11

  var td100 = document.createElement('td');
  td100.setAttribute('colspan', '4');
  td100.innerHTML = "RESULTATS SEMESTRE 1";
  var td101 = document.createElement('td');
  td101.setAttribute("id", "resultat-coef");
  var td102 = document.createElement('td');
  td102.setAttribute("id", "resultat-total");
  var td103 = document.createElement('td');
  td103.setAttribute("id", "resultat-moyenne");
  var td104 = document.createElement('td');
  td104.setAttribute("id", "resultat-rang");
  var td105 = document.createElement('td');
  td105.setAttribute("colspan", "2");
  td105.setAttribute("id", "resultat");
  td105.innerHTML = "Total Cr\xE9dits Semestre 1";
  var td106 = document.createElement('td');
  td106.setAttribute("id", "resultat-crédits");
  var tr11 = document.createElement('tr');
  tr11.appendChild(td100);
  tr11.appendChild(td101);
  tr11.appendChild(td102);
  tr11.appendChild(td103);
  tr11.appendChild(td104);
  tr11.appendChild(td105);
  tr11.appendChild(td106); //tbody

  var tbody = document.createElement('tbody');
  tbody.setAttribute('id', 'tbody01');
  tbody.appendChild(tr2);
  tbody.appendChild(tr3);
  tbody.appendChild(tr4);
  tbody.appendChild(tr5);
  tbody.appendChild(tr8);
  tbody.appendChild(tr9);
  tbody.appendChild(tr11);
  var table1 = document.createElement('table');
  table1.setAttribute('class', 'table-1');
  table1.appendChild(thead1);
  table1.appendChild(tbody); //table3
  //thead2

  var tr12 = document.createElement('tr');

  for (i = 0; i <= 11; i++) {
    var th = document.createElement('th');
    th.setAttribute('scope', 'col');

    if (i == 0) {
      th.innerHTML = "&nbsp;&nbsp;";
    }

    tr12.appendChild(th);
  }

  var thead2 = document.createElement('thead');
  thead2.appendChild(tr12); //tbody
  //Line 1

  var tr13 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne de Classe de l'\xE9tudiant :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Maximum :";
    }

    if (i == 7) {
      td.innerHTML = "Retard :";
    }

    tr13.appendChild(td);
  } //Line 2


  var tr14 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
      td.innerHTML = "Moyenne G\xE9n\xE9rale de la classe :";
    }

    if (i == 2) {
      td.innerHTML = "/ 20";
    }

    if (i == 3) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Minimum :";
    }

    if (i == 7) {
      td.innerHTML = "Absences:";
    }

    tr14.appendChild(td);
  } //Line 3


  var tr15 = document.createElement('tr');

  for (i = 0; i <= 8; i++) {
    var td = document.createElement('td');

    if (i == 1) {
      td.setAttribute('colspan', '3');
    }

    if (i == 4) {
      td.setAttribute('colspan', '2');
      td.innerHTML = "Rang :";
    }

    if (i == 5) {
      td.innerHTML = " sur ";
    }

    tr15.appendChild(td);
  } //Line 4


  var tbody3 = document.createElement('tbody');
  tbody3.setAttribute('id', 'tbody-3');
  tbody3.appendChild(tr13);
  tbody3.appendChild(tr14);
  tbody3.appendChild(tr15);
  var table3 = document.createElement('table');
  table3.setAttribute('id', 'table-3');
  table3.appendChild(thead2);
  table3.appendChild(tbody3);
  var semestreResult = document.createElement('div');
  semestreResult.setAttribute('id', 'semester-result');
  semestreResult.appendChild(table1);
  semestreResult.appendChild(table3);
  var main = document.createElement('main');
  main.appendChild(bullchecktitle);
  main.appendChild(infostudent);
  main.appendChild(semestreResult);
  var visa = document.createElement('div');
  visa.setAttribute('class', 'visa');
  visa.innerHTML = "VISA CHEF ETABLISSEMENT";
  var footer = document.createElement('footer');
  footer.appendChild(visa);
  containerbull = document.createElement('div');
  containerbull.setAttribute('class', 'container-bull');
  containerbull.appendChild(header);
  containerbull.appendChild(hr);
  containerbull.appendChild(main);
  containerbull.appendChild(footer);
  /*body=document.getElementsByTagName('body')
  body[0].appendChild(containerbull)*/

  return containerbull;
}
/**FONCTION BULLETIN MDS */


function BullMDS1(clone) {
  //TRI DES MATIERES
  a =
  /*[...*/
  mydata[4]; //]

  var sort111 = epuration(a);
  b = _toConsumableArray(mydata[5]);
  var sort111b = epuration(b);
  c = _toConsumableArray(mydata[6]);
  var sort112 = epuration(c);
  d = _toConsumableArray(mydata[7]);
  var sort112b = epuration(d);
  e = _toConsumableArray(mydata[8]);
  var sort113 = epuration(e);
  f = _toConsumableArray(mydata[9]);
  var sort114 = epuration(f);
  g = _toConsumableArray(mydata[10]);
  var sort115 = epuration(g);
  h = _toConsumableArray(mydata[11]);
  var sort116 = epuration(h);
  j = _toConsumableArray(mydata[12]);
  var sort117 = epuration(j);
  k = _toConsumableArray(mydata[13]);
  var sort117b = epuration(k); //DONNEES RECUPEREES DE LA BD

  infoEtudiant = mydata[1];
  var coefUe = mydata[2];
  var creditUe = mydata[3];
  var mds111 = mydata[4];
  var mds111b = mydata[5];
  var mds112 = mydata[6];
  var mds112b = mydata[7];
  var mds113 = mydata[8];
  var mds114 = mydata[9];
  var mds115 = mydata[10];
  var mds116 = mydata[11];
  var mds117 = mydata[12];
  var mds117b = mydata[13]; //Info Utilisateur

  info1 = clone.children[2].children[1].children[0];

  for (j = 2; j <= info1.childElementCount - 1; j++) {
    if (j == 2) {
      info1.children[j].innerHTML = info1.children[j].innerHTML + " ".concat(infoEtudiant[i]['nom']);
    }

    if (j == 3) {
      info1.children[j].innerHTML = info1.children[j].innerHTML + " ".concat(infoEtudiant[i]['prenom']);
    } //if(j==4){info1.children[j].innerHTML = info1.children[j].innerHTML +' er'}

  }

  info2 = clone.children[2].children[1].children[1];

  for (j = 1; j <= info2.childElementCount - 1; j++) {
    if (j == 1) {
      info2.children[j].innerHTML = info2.children[j].innerHTML + " ".concat(infoEtudiant[i]['matricule']);
    }

    if (j == 2) {
      info2.children[j].innerHTML = info2.children[j].innerHTML + " ".concat(infoEtudiant[i]['date_naissance']);
    }

    if (j == 3) {
      info2.children[j].innerHTML = info2.children[j].innerHTML + " ".concat(infoEtudiant[i]['lieu_naissance']);
    } //if(j==4){info1.children[j].innerHTML = info1.children[j].innerHTML +` ${infoEtudiant[i]['anneeaca']}`} //Année Academique

  } //Tableau de notes


  var tbody = clone.children[2].children[2].children[0].children[1]; //LIGNE MDS11

  var ligneMDS111 = tbody.children[0];

  for (j = 0; j <= ligneMDS111.childElementCount - 1; j++) {
    if (j == 4) {
      ligneMDS111.children[j].innerHTML = mds111[i]['note_Examen'];
    } //note math


    if (j == 5) {
      ligneMDS111.children[j].innerHTML = coefUe[0]['coefficient'];
    } //coef math


    if (j == 6) {
      val = ligneMDS111.children[4].innerHTML * ligneMDS111.children[5].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS111.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 7) {
      ligneMDS111.children[j].innerHTML = Moyenne4(ligneMDS111.children[6].innerHTML, mds111b[i]['note_Examen'] * coefUe[1]['coefficient'], mds112[i]['note_Examen'] * coefUe[2]['coefficient'], mds112b[i]['note_Examen'] * coefUe[3]['coefficient'], coefUe[0]['coefficient'] + coefUe[1]['coefficient'] + coefUe[2]['coefficient'] + coefUe[3]['coefficient']);
    } //moyenne donc (totalmath + totalinfo)/2


    if (j == 8) {
      ligneMDS111.children[j].innerHTML = sort111.indexOf(mds111[i]['note_Examen']) + 1;
      /*ligneMDS111.children[j].innerHTML =  mds1sort.indexof(mds111[i]['note_Examen'])*/
    } //Rang


    if (j == 9) {
      if (ligneMDS111.children[4].innerHTML >= 10) {
        ligneMDS111.children[9].innerHTML = "VALIDEE";
      } else {
        ligneMDS111.children[9].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 10) {} //Session


    if (j == 11) {
      if (mds111[i]["note_Examen"] >= 10 && mds111b[i]['note_Examen'] >= 10) {
        ligneMDS111.children[j].innerHTML = creditUe[0]['nombre_credit'];
      } else {
        ligneMDS111.children[j].innerHTML = 0;
      }
    } //Crédits

  } //MoyenneEtud[1]= 
  //LIGNE MDS11b


  ligneMDS111b = tbody.children[1];

  for (j = 0; j <= ligneMDS111b.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS111b.children[j].innerHTML = mds111b[i]['note_Examen'];
    } //note info


    if (j == 3) {
      ligneMDS111b.children[j].innerHTML = coefUe[1]['coefficient'];
    } //coef info


    if (j == 4) {
      val = ligneMDS111b.children[2].innerHTML * ligneMDS111b.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS111b.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS111b.children[j].innerHTML = sort111b.indexOf(mds111b[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS111b.children[2].innerHTML >= 10) {
        ligneMDS111b.children[6].innerHTML = "VALIDEE";
      } else {
        ligneMDS111b.children[6].innerHTML = "NON VALIDEE";
      }
    }

    if (j == 7) {} //Session


    if (j == 8) {
      if (mds111[i]["note_Examen"] >= 10 && mds111b[i]['note_Examen'] >= 10) {
        ligneMDS111b.children[j].innerHTML = creditUe[1]['nombre_credit'];
      } else {
        ligneMDS111b.children[j].innerHTML = 0;
      }
    } //Crédits

  } //LIGNE MDS112


  var ligneMDS112 = tbody.children[2];

  for (j = 0; j <= ligneMDS112.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS112.children[j].innerHTML = mds112[i]['note_Examen'];
    } //note info


    if (j == 3) {
      ligneMDS112.children[j].innerHTML = coefUe[2]['coefficient'];
    } //coef info


    if (j == 4) {
      val = ligneMDS112.children[2].innerHTML * ligneMDS112.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS112.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS112.children[j].innerHTML = sort112.indexOf(mds112[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS112.children[2].innerHTML >= 10) {
        ligneMDS112.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS112.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {} //Session


    if (j == 8) {
      if (ligneMDS112.children[2].innerHTML >= 10 && mds112b[i]['note_Examen'] >= 10) {
        ligneMDS112.children[j].innerHTML = creditUe[2]['nombre_credit'];
      } else {
        ligneMDS112.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE MDS112


  var ligneMDS112b = tbody.children[3];

  for (j = 0; j <= ligneMDS112b.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS112b.children[j].innerHTML = mds112b[i]['note_Examen'];
    } //note info


    if (j == 3) {
      ligneMDS112b.children[j].innerHTML = coefUe[3]['coefficient'];
    } //coef info


    if (j == 4) {
      val = ligneMDS112b.children[2].innerHTML * ligneMDS112b.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS112b.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS112b.children[j].innerHTML = sort112b.indexOf(mds112b[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS112b.children[2].innerHTML >= 10) {
        ligneMDS112b.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS112b.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {} //Session


    if (j == 8) {
      if (ligneMDS112b.children[2].innerHTML >= 10) {
        ligneMDS112b.children[j].innerHTML = creditUe[2]['nombre_credit'];
      } else {
        ligneMDS112b.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE MDS113


  var ligneMDS113 = tbody.children[4];

  for (j = 0; j <= ligneMDS113.childElementCount - 1; j++) {
    if (j == 3) {
      ligneMDS113.children[j].innerHTML = mds113[i]['note_Examen'];
    } //note math


    if (j == 4) {
      ligneMDS113.children[j].innerHTML = coefUe[4]['coefficient'];
    } //coef math


    if (j == 5) {
      val = ligneMDS113.children[3].innerHTML * ligneMDS113.children[4].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS113.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 6) {
      ligneMDS113.children[j].innerHTML = Moyenne4(ligneMDS113.children[5].innerHTML, mds114[i]['note_Examen'] * coefUe[5]['coefficient'], mds115[i]['note_Examen'] * coefUe[6]['coefficient'], mds116[i]['note_Examen'] * coefUe[7]['coefficient'], coefUe[4]['coefficient'] + coefUe[5]['coefficient'] + coefUe[6]['coefficient'] + coefUe[7]['coefficient']);
    } //moyenne donc (totalmath + totalinfo)/2


    if (j == 7) {
      ligneMDS113.children[j].innerHTML = sort113.indexOf(mds113[i]['note_Examen']) + 1;
    } //Rang


    if (j == 8) {
      if (ligneMDS113.children[3].innerHTML >= 10) {
        ligneMDS113.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS113.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 9) {}

    if (j == 10) {
      if (mds113[i]["note_Examen"] >= 10) {
        ligneMDS113.children[j].innerHTML = creditUe[3]['nombre_credit'];
      } else {
        ligneMDS113.children[j].innerHTML = 0;
      }
    } //Crédits

  } //LINE MDS114


  var ligneMDS114 = tbody.children[5];

  for (j = 0; j <= ligneMDS114.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS114.children[j].innerHTML = mds114[i]['note_Examen'];
    } //note info


    if (j == 3) {
      ligneMDS114.children[j].innerHTML = coefUe[5]['coefficient'];
    } //coef info


    if (j == 4) {
      val = ligneMDS114.children[2].innerHTML * ligneMDS114.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS114.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS114.children[j].innerHTML = sort114.indexOf(mds114[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS114.children[2].innerHTML >= 10) {
        ligneMDS114.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS114.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {} //Session


    if (j == 8) {
      if (ligneMDS114.children[2].innerHTML >= 10) {
        ligneMDS114.children[j].innerHTML = creditUe[4]['nombre_credit'];
      } else {
        ligneMDS114.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LINE MDS115


  var ligneMDS115 = tbody.children[6];

  for (j = 0; j <= ligneMDS115.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS115.children[j].innerHTML = mds115[i]['note_Examen'];
    } //note info


    if (j == 3) {
      ligneMDS115.children[j].innerHTML = coefUe[6]['coefficient'];
    } //coef info


    if (j == 4) {
      val = ligneMDS115.children[2].innerHTML * ligneMDS115.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS115.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS115.children[j].innerHTML = sort115.indexOf(mds115[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS115.children[2].innerHTML >= 10) {
        ligneMDS115.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS115.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {} //Session


    if (j == 8) {
      if (ligneMDS115.children[2].innerHTML >= 10) {
        ligneMDS115.children[j].innerHTML = creditUe[5]['nombre_credit'];
      } else {
        ligneMDS115.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LINE MD16


  var ligneMDS116 = tbody.children[7];

  for (j = 0; j <= ligneMDS116.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS116.children[j].innerHTML = mds116[i]['note_Examen'];
    } //note info


    if (j == 3) {
      ligneMDS116.children[j].innerHTML = coefUe[7]['coefficient'];
    } //coef info


    if (j == 4) {
      val = ligneMDS116.children[2].innerHTML * ligneMDS116.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS116.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS116.children[j].innerHTML = sort116.indexOf(mds116[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS116.children[2].innerHTML >= 10) {
        ligneMDS116.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS116.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {} //Session


    if (j == 8) {
      if (ligneMDS116.children[2].innerHTML >= 10) {
        ligneMDS116.children[j].innerHTML = creditUe[6]['nombre_credit'];
      } else {
        ligneMDS116.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LINE 17


  var ligneMDS117 = tbody.children[8];

  for (j = 0; j <= ligneMDS117.childElementCount - 1; j++) {
    if (j == 3) {
      ligneMDS117.children[j].innerHTML = mds117[i]['note_Examen'];
    } //note math


    if (j == 4) {
      ligneMDS117.children[j].innerHTML = coefUe[8]['coefficient'];
    } //coef math


    if (j == 5) {
      val = ligneMDS117.children[3].innerHTML * ligneMDS117.children[4].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS117.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 6) {
      ligneMDS117.children[j].innerHTML = Moyenne2(ligneMDS117.children[5].innerHTML, mds117b[i]['note_Examen'] * coefUe[9]['coefficient'], coefUe[8]['coefficient'] + coefUe[9]['coefficient']);
    } //moyenne donc (totalmath + totalinfo)/2


    if (j == 7) {
      ligneMDS117.children[j].innerHTML = sort117.indexOf(mds117[i]['note_Examen']) + 1;
    } //Rang


    if (j == 8) {
      if (ligneMDS117.children[3].innerHTML >= 10) {
        ligneMDS117.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS117.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 9) {}

    if (j == 10) {
      if (mds117[i]["note_Examen"] >= 10 && mds117b[i]['note_Examen'] >= 10) {
        ligneMDS117.children[j].innerHTML = creditUe[8]['nombre_credit'];
      } else {
        ligneMDS117.children[j].innerHTML = 0;
      }
    } //Crédits

  } //LINE 17b


  var ligneMDS117b = tbody.children[9];

  for (j = 0; j <= ligneMDS117b.childElementCount - 1; j++) {
    if (j == 2) {
      ligneMDS117b.children[j].innerHTML = mds117b[i]['note_Examen'];
    } //note math


    if (j == 3) {
      ligneMDS117b.children[j].innerHTML = coefUe[9]['coefficient'];
    } //coef math


    if (j == 4) {
      val = ligneMDS117b.children[3].innerHTML * ligneMDS117b.children[2].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneMDS117b.children[j].innerHTML = val;
    } //total note math * coef


    if (j == 5) {
      ligneMDS117b.children[j].innerHTML = sort117b.indexOf(mds117b[i]['note_Examen']) + 1;
    } //Rang


    if (j == 6) {
      if (ligneMDS117b.children[2].innerHTML >= 10) {
        ligneMDS117b.children[j].innerHTML = "VALIDEE";
      } else {
        ligneMDS117b.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {} //Session

  } //LINE DEs RESULTATS


  resultat = tbody.children[10];

  for (j = 0; j <= resultat.childElementCount - 1; j++) {
    if (j == 1) {
      resultat.children[1].innerHTML = sommeInt1(ligneMDS111.children[5].innerHTML, ligneMDS111b.children[3].innerHTML, ligneMDS112.children[3].innerHTML, ligneMDS112b.children[3].innerHTML, ligneMDS113.children[4].innerHTML, ligneMDS114.children[3].innerHTML, ligneMDS115.children[3].innerHTML, ligneMDS116.children[3].innerHTML, ligneMDS117.children[4].innerHTML, ligneMDS117b.children[3].innerHTML);
    }

    if (j == 2) {
      resultat.children[2].innerHTML = sommeFloat(ligneMDS111b.children[4].innerHTML, ligneMDS111.children[6].innerHTML, ligneMDS112.children[4].innerHTML, ligneMDS113.children[5].innerHTML, ligneMDS114.children[4].innerHTML, ligneMDS115.children[4].innerHTML, ligneMDS116.children[4].innerHTML, ligneMDS117.children[5].innerHTML, ligneMDS112b.children[4].innerHTML, ligneMDS117b.children[4].innerHTML);
    }

    if (j == 3) {
      val = resultat.children[2].innerHTML / resultat.children[1].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      resultat.children[j].innerHTML = val;
    }

    if (j == 6) {
      resultat.children[6].innerHTML = sommeInt(ligneMDS111.children[11].innerHTML, ligneMDS112.children[8].innerHTML, ligneMDS113.children[10].innerHTML, ligneMDS114.children[8].innerHTML, ligneMDS115.children[8].innerHTML, ligneMDS116.children[8].innerHTML, ligneMDS117.children[10].innerHTML);
    }
    /**TOtal Crédit */

  } //Tbody


  var body3 = clone.children[2].children[2].children[1].children[1]; //LIGNE 0

  var ligne0 = body3.children[0];

  for (j = 0; j <= ligne0.childElementCount - 1; j++) {
    if (j == 2) {
      ligne0.children[2].innerHTML = "".concat(resultat.children[3].innerHTML, " / 20");
    }

    if (j == 4) {
      ligne0.children[j].innerHTML = "X / 20";
    }
  } //LIGNE 1


  var ligne1 = body3.children[1];

  for (j = 0; j <= ligne1.childElementCount - 1; j++) {
    if (j == 2) {
      ligne1.children[j].innerHTML = "X / 20";
    }

    if (j == 4) {
      ligne1.children[j].innerHTML = "X / 20";
    }
  } //LLIGNE 2


  var ligne2 = body3.children[2];

  for (j = 0; j <= ligne1.childElementCount - 1; j++) {
    if (j == 5) {
      ligne2.children[j].innerHTML = " sur ".concat(mydata[1].length);
    }

    if (j == 4) {}
  }

  return clone;
}
/**FONCTION BULLETIN STAPS1 */


function BullSTAPS1(clone, i) {
  //DONNEES RECUPEREES DE LA BD
  listStudent = mydata[1]; //Info Utilisateur

  info1 = clone.children[2].children[1].children[0];
  info1.children[2].innerHTML = info1.children[2].innerHTML + " ".concat(listStudent[i][0]['nom']);
  info1.children[3].innerHTML = info1.children[3].innerHTML + " ".concat(listStudent[i][0]['prenom']);
  info2 = clone.children[2].children[1].children[1];
  info2.children[1].innerHTML = info2.children[1].innerHTML + " ".concat(listStudent[i][0]['matricule']);
  info2.children[2].innerHTML = info2.children[2].innerHTML + " ".concat(listStudent[i][0]['date_naissance']);
  info2.children[3].innerHTML = info2.children[3].innerHTML + " ".concat(listStudent[i][0]['lieu_naissance']);
  info2.children[4].innerHTML = info2.children[4].innerHTML + " 2022-2023"; //RESULTATS

  var tbody = clone.children[2].children[2].children[0].children[1]; //LIGNE EPS111

  var ligneEPS111 = tbody.children[0];

  for (j = 0; j <= ligneEPS111.childElementCount - 1; j++) {
    if (j == 4) {
      ligneEPS111.children[j].innerHTML = listStudent[i][1][0];
    } //note 


    if (j == 5) {
      ligneEPS111.children[j].innerHTML = listStudent[i][1][1];
    } //coef


    if (j == 6) {
      val = ligneEPS111.children[4].innerHTML * ligneEPS111.children[5].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneEPS111.children[j].innerHTML = val;
    } //total note  * coef


    if (j == 7) {
      ligneEPS111.children[j].innerHTML = listStudent[i][1][3];
    } //moyenne donc (totalmath + totalinfo)/2


    if (j == 8) {
      ligneEPS111.children[j].innerHTML = listStudent[i][1][4];
    } //Rang


    if (j == 9) {
      if (listStudent[i][1][5]) {
        ligneEPS111.children[j].innerHTML = "VALIDEE";
        ligneEPS111.children[9].innerHTML = "VALIDEE";
      } else {
        ligneEPS111.children[9].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 10) {
      ligneEPS111.children[j].innerHTML = mydata[4];
    } //Session


    if (j == 11) {
      if (listStudent[i][1][0] >= 10) {
        ligneEPS111.children[j].innerHTML = listStudent[i][1][6];
      } else {
        ligneEPS111.children[j].innerHTML = 0;
      }
    } //Crédits

  } //LIGNE EPS112


  ligneEPS112 = tbody.children[1];

  for (j = 0; j <= ligneEPS112.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS112.children[j].innerHTML = listStudent[i][2][0];
    } //note info


    if (j == 3) {
      ligneEPS112.children[j].innerHTML = listStudent[i][2][1];
    } //coef info


    if (j == 4) {
      ligneEPS112.children[j].innerHTML = listStudent[i][2][2];
    } //val=ligneEPS112.children[2].innerHTML*ligneEPS112.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val); ligneEPS112.children[j].innerHTML = val}//total note math * coef


    if (j == 5) {
      ligneEPS112.children[j].innerHTML = listStudent[i][2][4];
    } //Rang


    if (j == 6) {
      if (listStudent[i][2][5]) {
        ligneEPS112.children[6].innerHTML = "VALIDEE";
      } else {
        ligneEPS112.children[6].innerHTML = "NON VALIDEE";
      }
    }

    if (j == 7) {
      ligneEPS112.children[j].innerHTML = mydata[4];
    } //Session


    if (j == 8) {
      if (listStudent[i][2][5]) {
        ligneEPS112.children[j].innerHTML = listStudent[i][2][6];
      } else {
        ligneEPS112.children[j].innerHTML = 0;
      }
    } //Crédits

  } //LIGNE EPS113


  var ligneEPS113 = tbody.children[2];

  for (j = 0; j <= ligneEPS113.childElementCount - 1; j++) {
    if (j == 3) {
      ligneEPS113.children[j].innerHTML = listStudent[i][3][0];
    } //note info


    if (j == 4) {
      ligneEPS113.children[j].innerHTML = listStudent[i][3][1];
    } //coef info


    if (j == 5) {
      val = ligneEPS113.children[2].innerHTML * ligneEPS113.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneEPS113.children[j].innerHTML = listStudent[i][3][2];
    } //total note math * coef


    if (j == 6) {
      ligneEPS113.children[j].innerHTML = listStudent[i][3][3];
    } //


    if (j == 7) {
      ligneEPS113.children[j].innerHTML = listStudent[i][3][4];
    }

    if (j == 8) {
      if (listStudent[i][3][5]) {
        ligneEPS113.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS113.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 9) {
      ligneEPS113.children[j].innerHTML = mydata[4];
    } // Session


    if (j == 10) {
      if (listStudent[i][3][5]) {
        ligneEPS113.children[j].innerHTML = listStudent[i][3][6];
      } else {
        ligneEPS113.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS114


  var ligneEPS114 = tbody.children[3];

  for (j = 0; j <= ligneEPS114.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS114.children[j].innerHTML = listStudent[i][4][0];
    } //note info


    if (j == 3) {
      ligneEPS114.children[j].innerHTML = listStudent[i][4][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS114.children[2].innerHTML*ligneEPS114.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS114.children[j].innerHTML = listStudent[i][4][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS114.children[j].innerHTML = listStudent[i][4][4];
    } //


    if (j == 6) {
      if (listStudent[i][4][5]) {
        ligneEPS114.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS114.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS114.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][4][5]) {
        ligneEPS114.children[j].innerHTML = listStudent[i][4][6];
      } else {
        ligneEPS114.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS115a


  var ligneEPS115a = tbody.children[4];

  for (j = 0; j <= ligneEPS115a.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS115a.children[j].innerHTML = listStudent[i][5][0];
    } //note info


    if (j == 3) {
      ligneEPS115a.children[j].innerHTML = listStudent[i][5][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS115a.children[2].innerHTML*ligneEPS115a.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS115a.children[j].innerHTML = listStudent[i][5][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS115a.children[j].innerHTML = listStudent[i][5][4];
    } //


    if (j == 6) {
      if (listStudent[i][5][5]) {
        ligneEPS115a.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS115a.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS115a.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][5][5]) {
        ligneEPS115a.children[j].innerHTML = listStudent[i][5][6];
      } else {
        ligneEPS115a.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS115b


  var ligneEPS115b = tbody.children[5];

  for (j = 0; j <= ligneEPS115b.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS115b.children[j].innerHTML = listStudent[i][6][0];
    } //note info


    if (j == 3) {
      ligneEPS115b.children[j].innerHTML = listStudent[i][6][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS115b.children[2].innerHTML*ligneEPS115b.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS115b.children[j].innerHTML = listStudent[i][6][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS115b.children[j].innerHTML = listStudent[i][5][4];
    } //


    if (j == 6) {
      if (listStudent[i][6][5]) {
        ligneEPS115b.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS115b.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS115b.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][6][5]) {
        ligneEPS115b.children[j].innerHTML = listStudent[i][6][6];
      } else {
        ligneEPS115b.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS115j


  var ligneEPS115j = tbody.children[6];

  for (j = 0; j <= ligneEPS115j.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS115j.children[j].innerHTML = listStudent[i][7][0];
    } //note info


    if (j == 3) {
      ligneEPS115j.children[j].innerHTML = listStudent[i][7][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS115j.children[2].innerHTML*ligneEPS115j.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS115j.children[j].innerHTML = listStudent[i][7][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS115j.children[j].innerHTML = listStudent[i][7][4];
    } //


    if (j == 6) {
      if (listStudent[i][7][5]) {
        ligneEPS115j.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS115j.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS115j.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][7][5]) {
        ligneEPS115j.children[j].innerHTML = listStudent[i][7][6];
      } else {
        ligneEPS115j.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS115l


  var ligneEPS115l = tbody.children[7];

  for (j = 0; j <= ligneEPS115l.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS115l.children[j].innerHTML = listStudent[i][8][0];
    } //note info


    if (j == 3) {
      ligneEPS115l.children[j].innerHTML = listStudent[i][8][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS115l.children[2].innerHTML*ligneEPS115l.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS115l.children[j].innerHTML = listStudent[i][8][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS115l.children[j].innerHTML = listStudent[i][8][4];
    } //


    if (j == 6) {
      if (listStudent[i][8][5]) {
        ligneEPS115l.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS115l.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS115l.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][8][5]) {
        ligneEPS115l.children[j].innerHTML = listStudent[i][8][6];
      } else {
        ligneEPS115l.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS116


  var ligneEPS116 = tbody.children[8];

  for (j = 0; j <= ligneEPS116.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS116.children[j].innerHTML = listStudent[i][9][0];
    } //note info


    if (j == 3) {
      ligneEPS116.children[j].innerHTML = listStudent[i][9][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS116.children[2].innerHTML*ligneEPS116.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS116.children[j].innerHTML = listStudent[i][9][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS116.children[j].innerHTML = listStudent[i][9][4];
    } //


    if (j == 6) {
      if (listStudent[i][9][5]) {
        ligneEPS116.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS116.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS116.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][9][5]) {
        ligneEPS116.children[j].innerHTML = listStudent[i][9][6];
      } else {
        ligneEPS116.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS117


  var ligneEPS117 = tbody.children[9];

  for (j = 0; j <= ligneEPS117.childElementCount - 1; j++) {
    if (j == 3) {
      ligneEPS117.children[j].innerHTML = listStudent[i][10][0];
    } //note info


    if (j == 4) {
      ligneEPS117.children[j].innerHTML = listStudent[i][10][1];
    } //coef info


    if (j == 5) {
      val = ligneEPS117.children[2].innerHTML * ligneEPS117.children[3].innerHTML;
      val = val.toFixed(2);
      val = parseFloat(val);
      ligneEPS117.children[j].innerHTML = listStudent[i][10][2];
    } //total note math * coef


    if (j == 6) {
      ligneEPS117.children[j].innerHTML = listStudent[i][10][3];
    } //


    if (j == 7) {
      ligneEPS117.children[j].innerHTML = listStudent[i][10][4];
    }

    if (j == 8) {
      if (listStudent[i][10][5]) {
        ligneEPS117.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS117.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 9) {
      ligneEPS117.children[j].innerHTML = mydata[4];
    } // Session


    if (j == 10) {
      if (listStudent[i][10][5]) {
        ligneEPS117.children[j].innerHTML = listStudent[i][10][6];
      } else {
        ligneEPS117.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS118


  var ligneEPS118 = tbody.children[10];

  for (j = 0; j <= ligneEPS118.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS118.children[j].innerHTML = listStudent[i][11][0];
    } //note info


    if (j == 3) {
      ligneEPS118.children[j].innerHTML = listStudent[i][11][1];
    } //coef info


    if (j == 4) {
      /*val=ligneEPS118.children[2].innerHTML*ligneEPS118.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/
      ligneEPS118.children[j].innerHTML = listStudent[i][11][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS118.children[j].innerHTML = listStudent[i][11][4];
    } //


    if (j == 6) {
      if (listStudent[i][11][5]) {
        ligneEPS118.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS118.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS118.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][11][5]) {
        ligneEPS118.children[j].innerHTML = listStudent[i][11][6];
      } else {
        ligneEPS118.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LIGNE EPS119


  var ligneEPS119 = tbody.children[11];

  for (j = 0; j <= ligneEPS119.childElementCount - 1; j++) {
    if (j == 2) {
      ligneEPS119.children[j].innerHTML = listStudent[i][12][0];
    } //note info


    if (j == 3) {
      ligneEPS119.children[j].innerHTML = listStudent[i][12][1];
    } //coef info


    if (j == 4) {
      ligneEPS119.children[j].innerHTML = listStudent[i][1][2];
    } //total note math * coef


    if (j == 5) {
      ligneEPS119.children[j].innerHTML = listStudent[i][11][4];
    } //


    if (j == 6) {
      if (listStudent[i][12][5]) {
        ligneEPS119.children[j].innerHTML = "VALIDEE";
      } else {
        ligneEPS119.children[j].innerHTML = "NON VALIDEE";
      }
    } //Mention


    if (j == 7) {
      ligneEPS119.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][12][5]) {
        ligneEPS119.children[j].innerHTML = listStudent[i][12][6];
      } else {
        ligneEPS119.children[j].innerHTML = 0;
      }
    } //nombre_crédits

  } //LINE DEs RESULTATS


  resultat = tbody.children[12];

  for (j = 0; j <= resultat.childElementCount - 1; j++) {
    if (j == 1) {
      resultat.children[1].innerHTML = listStudent[i][13][0];
    }

    if (j == 2) {
      resultat.children[2].innerHTML = listStudent[i][13][1];
    }

    if (j == 3) {
      resultat.children[j].innerHTML = listStudent[i][13][2];
    }

    if (j == 4) {
      resultat.children[j].innerHTML = mydata[2].indexOf(listStudent[i][13][2]) + 1;
    }

    if (j == 6) {
      resultat.children[6].innerHTML = sommeInt9(ligneEPS111.children[11].innerHTML, ligneEPS112.children[8].innerHTML, ligneEPS113.children[10].innerHTML, ligneEPS114.children[8].innerHTML, ligneEPS115a.children[8].innerHTML, ligneEPS116.children[8].innerHTML, ligneEPS117.children[10].innerHTML, ligneEPS118.children[8].innerHTML, ligneEPS119.children[8].innerHTML);
    }
    /**TOtal Crédit */

  } //Tbody


  var body3 = clone.children[2].children[2].children[1].children[1]; //LIGNE 0

  var ligne0 = body3.children[0];

  for (j = 0; j <= ligne0.childElementCount - 1; j++) {
    if (j == 2) {
      ligne0.children[2].innerHTML = "".concat(listStudent[i][13][2], " / 20");
    }

    if (j == 4) {
      ligne0.children[j].innerHTML = "".concat(mydata[2][0], " / 20");
    }
  } //LIGNE 1


  var ligne1 = body3.children[1];

  for (j = 0; j <= ligne1.childElementCount - 1; j++) {
    if (j == 2) {
      ligne1.children[j].innerHTML = "".concat(mydata[3], " / 20");
    }

    if (j == 4) {
      var note_length = mydata[2].length - 1;
      ligne1.children[j].innerHTML = "".concat(mydata[2][note_length], " / 20");
    } //

  } //LLIGNE 2


  var ligne2 = body3.children[2];

  for (j = 0; j <= ligne1.childElementCount - 1; j++) {
    if (j == 5) {
      ligne2.children[j].innerHTML = "".concat(resultat.children[4].innerHTML, " sur ").concat(mydata[1].length);
    }

    if (j == 4) {}
  }

  return clone;
}
/**FONCTION BULLETIN STAPS2 */


function BullSTAPS2(clone) {} //FONCTIONS


function Moyenne3(a, b, c, coef) {
  a = parseFloat(a);
  b = parseFloat(b);
  c = parseFloat(c);
  result = (a + b + c) / coef;
  result = result.toFixed(2);
  result = parseFloat(result);
  return result;
}

function Moyenne2(a, b, coef) {
  a = parseFloat(a);
  b = parseFloat(b);
  result = (a + b) / coef;
  result = result.toFixed(2);
  result = parseFloat(result);
  return result;
}

function Moyenne4(a, b, c, d, coef) {
  a = parseFloat(a);
  b = parseFloat(b);
  c = parseFloat(c);
  d = parseFloat(d);
  result = (a + b + c + d) / coef;
  result = result.toFixed(2);
  result = parseFloat(result);
  return result;
}

function sommeInt1(a, b, c, d, e, f, g, h, i, j) {
  a = parseInt(a);
  b = parseInt(b);
  c = parseInt(c);
  d = parseInt(d);
  e = parseInt(e);
  f = parseInt(f);
  g = parseInt(g);
  h = parseInt(h);
  i = parseInt(i);
  j = parseInt(j);
  result = a + b + c + d + e + f + g + h + i + j;
  return result;
}

function sommeInt2(a, b) {
  a = parseInt(a);
  b = parseInt(b);
  result = a + b;
  return result;
}

function sommeInt(a, b, c, d, e, f, g) {
  a = parseInt(a);
  b = parseInt(b);
  c = parseInt(c);
  d = parseInt(d);
  e = parseInt(e);
  f = parseInt(f);
  g = parseInt(g);
  result = a + b + c + d + e + f + g;
  return result;
}

function sommeInt9(a, b, c, d, e, f, g, h, i) {
  a = parseInt(a);
  b = parseInt(b);
  c = parseInt(c);
  d = parseInt(d);
  e = parseInt(e);
  f = parseInt(f);
  g = parseInt(g);
  h = parseInt(h);
  i = parseInt(i);
  result = a + b + c + d + e + f + g + h + i;
  return result;
}

function sommeFloat(a, b, c, d, e, f, g, h) {
  a = parseFloat(a);
  b = parseFloat(b);
  c = parseFloat(c);
  d = parseFloat(d);
  e = parseFloat(e);
  f = parseFloat(f);
  g = parseFloat(g);
  h = parseFloat(h);
  result = a + b + c + d + e + f + g + h + i + j;
  result = result.toFixed(2);
  result = parseFloat(result);
  return result;
}

function triCroissant(b) {
  for (i = 0; i <= b.length; i++) {
    for (j = i + 1; j <= b.length; j++) {
      if (b[i] >= b[j]) {
        tmp = b[i];
        b[i] = b[j];
        b[j] = tmp;
      }
    }
  }

  return b;
}

function triDecroissant(b) {
  for (i = 0; i <= b.length; i++) {
    for (j = i + 1; j <= b.length; j++) {
      if (b[i] <= b[j]) {
        tmp = b[i];
        b[i] = b[j];
        b[j] = tmp;
      }
    }
  }

  return b;
}

function formatAsArray(b) {
  ar = [];

  for (var i = 0; i <= b.length; i++) {
    console.log(b[i]['note_Examen']);
  }

  return ar;
}

function epuration(a) {
  var sort111 = [];

  for (k = 0; k <= a.length - 1; k++) {
    sort111[k] = a[k]["note_Examen"];
  } //sort111 = triDecroissant(sort111)


  return sort111;
}

function stringToIntArray(a) {
  //val = []
  for (k = 0; k <= a.length - 1; k++) {
    tmp = parseFloat(a[k]);
    a[k] = tmp;
  }

  return a;
}