"use strict";

window.addEventListener('load', function () {
  //Recuperation de la variable des données
  mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
  console.log(mydata);

  function Page1() {
    listStudent = mydata[1];
    var page0 = document.getElementById('page');
    page0 = page0.cloneNode(true);
    page0.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE SYNTHESE 1<sup>er</sup> SEMESTRE MDS2  ".concat(mydata[9][0]['annee_academique']);
    bigtab = page0.children[0].children[2].children[1]; //page2.children[1].children[1].children[1]

    /*page = document.getElementById("page2")
    bigtab1 = page.children[1].children[1]*/
    //Tableau Sur lequel on ajoute les nouvelles lignes

    worktab = bigtab.children[1];
    worktab.children[0].children[0].innerHTML = "PROCES VERBAL MODULAIRE MDS2 ".concat(mydata[9][0]['annee_academique']); //worktab1 = bigtab1.children[1]
    //Ligne des 4 tableaux

    for (i = 0; i <= mydata[1].length - 1; i++) {
      temp = worktab.children[3].cloneNode(true); //temp1 = worktab1.children[3].cloneNode(true)
      //tab0

      tab0 = temp.children[0];
      tab01 = tab0.children.nested4;
      tab02 = tab01.children;
      tab03 = tab02['0'];
      tab04 = tab03.children;
      tab05 = tab04[0]; //good

      for (j = 0; j <= tab05.childElementCount - 1; j++) {
        if (j == 0) {
          tab05.cells[j].innerHTML = i + 1;
        }

        if (j == 1) {
          tab05.cells[j].innerHTML = listStudent[i][0]['nom'];
        }

        if (j == 2) {
          tab05.cells[j].innerHTML = listStudent[i][0]['prenom'];
        }

        if (j == 3) {
          tab05.cells[j].innerHTML = listStudent[i][0]['matricule'];
        }
      } //tab0 Page2
      //tab1


      tab1 = temp.children[1];
      tab11 = tab1.children.nested11;
      tab12 = tab11.children;
      tab13 = tab12['0'];
      tab14 = tab13.children;
      tab15 = tab14[0]; //good line

      for (j = 0; j <= tab15.childElementCount - 1; j++) {
        if (j == 0) {
          tab15.cells[j].innerHTML = listStudent[i][1][0];
        }

        ;

        if (j == 1) {
          tab15.cells[j].innerHTML = listStudent[i][2][0];
        }

        if (j == 2) {
          tab15.cells[j].innerHTML = listStudent[i][3][0];
        }

        if (j == 3) {
          tab15.cells[j].innerHTML = listStudent[i][4][0];
        }

        if (j == 4) {
          var uef12cr = listStudent[i][1][5]; //listStudent[i][1][6]
          //if ((listStudent[i][1][0] + listStudent[i][2][0]) < 20) { uef12cr = 0 }

          /*var uef2cr = listStudent[i][2][6]
          if (listStudent[i][2][0] < 10) { uef2cr = 0 }*/

          var uef34cr = listStudent[i][3][5]; //listStudent[i][3][6]
          //if ((listStudent[i][3][0] + listStudent[i][4][0]) < 20) { uef34cr = 0 }

          /*var uef2cr = listStudent[i][4][6]
          if (listStudent[i][4][0] < 10) { uef2cr = 0 }*/

          var moyuef = listStudent[i][1][3];

          if (moyuef >= 10 && listStudent[i][1][0] >= 7 && listStudent[i][2][0] >= 7 && listStudent[i][3][0] >= 7 && listStudent[i][4][0] >= 7) {
            //console.log('OK');
            moyuefcr = uef34cr + uef12cr;
          } else {
            moyuef = '--'; //moyuefcr = uef1cr + uef2cr
          }

          tab15.cells[j].innerHTML = moyuef; //listStudent[i][1][3];
        }

        if (j == 5) {
          tab15.cells[j].innerHTML = uef12cr + uef34cr;
        }
      } //tab2


      tab2 = temp.children[2];
      tab21 = tab2.children.nested22;
      tab22 = tab21.children['0'];
      tab23 = tab22.children['0'];

      for (j = 0; j <= tab23.childElementCount - 1; j++) {
        if (j == 0) {
          tab23.cells[j].innerHTML = listStudent[i][5][0];
        }

        ;

        if (j == 1) {
          tab23.cells[j].innerHTML = listStudent[i][6][0];
        }

        ;

        if (j == 2) {
          tab23.cells[j].innerHTML = listStudent[i][7][0];
        }

        ;

        if (j == 3) {
          tab23.cells[j].innerHTML = listStudent[i][8][0];
        }

        ;

        if (j == 4) {
          /*var uef56cr = listStudent[i][5][6]
          if ((listStudent[i][5][0] + listStudent[i][6][0]) < 20) { uef56cr = 0 }
            var uef78cr = listStudent[i][7][6]
          if ((listStudent[i][7][0] + listStudent[i][8][0]) < 20) { uef78cr = 0 }*/
          var uef5cr = listStudent[i][5][5]; //if ((listStudent[i][5][0]) < 10) { uef5cr = 0 }

          var uef6cr = listStudent[i][6][5]; //if ((listStudent[i][6][0]) < 10) { uef6cr = 0 }

          var uef7cr = listStudent[i][7][5]; //if ((listStudent[i][7][0]) < 10) { uef7cr = 0 }

          var uef8cr = listStudent[i][8][5]; //if ((listStudent[i][8][0]) < 10) { uef8cr = 0 }

          var moyuefcr = uef5cr + uef6cr + uef7cr + uef8cr; //listStudent[i][5][6] + listStudent[i][6][6] + listStudent[i][7][6] + listStudent[i][8][6]
          //if ((listStudent[i][5][0] + listStudent[i][6][0] + listStudent[i][7][0] + listStudent[i][8][0]) < 40) { uef5678cr = uef5cr + uef6cr + uef7cr + uef8cr }

          moyuep = listStudent[i][5][3];

          if (moyuep >= 10 && listStudent[i][5][0] >= 7 && listStudent[i][6][0] >= 7 && listStudent[i][7][0] >= 7 && listStudent[i][8][0] >= 7) {
            /*console.log('OK');
            moyuepcr = uef56cr + uef78cr*/
          } else {
            moyuep = '--'; //moyuefcr = uef5cr + uef6cr + uef7cr + uef8cr
          }

          tab23.cells[j].innerHTML = moyuep; //listStudent[i][5][3]
        }

        ;

        if (j == 5) {
          tab23.cells[j].innerHTML = moyuefcr;
        }

        ; //Crédits
      } //tab3


      tab3 = temp.children[3];
      tab31 = tab3.children.nested33;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        if (j == 0) {
          tab33.cells[j].innerHTML = listStudent[i][9][0];
        }

        ;

        if (j == 1) {
          tab33.cells[j].innerHTML = listStudent[i][10][0];
        }

        ;
        ;

        if (j == 2) {
          var uef9cr = listStudent[i][9][5]; //if ((listStudent[i][9][0]) < 10) { uef9cr = 0 }

          var uef10cr = listStudent[i][10][5]; //if ((listStudent[i][10][0]) < 10) { uef10cr = 0 }

          var uef910cr = uef9cr + uef10cr; //listStudent[i][10][6] + listStudent[i][9][6]
          //if ((listStudent[i][10][0] + listStudent[i][9][0]) < 20) { uef910cr = uef9cr + uef10cr }

          moyuet = listStudent[i][9][3];

          if (moyuet >= 10 && listStudent[i][9][0] >= 7 && listStudent[i][10][0] >= 7) {//moyuetcr = uef9cr + uef10cr
          } else {
            moyuet = '--'; //moyuefcr = uef1cr + uef2cr
          }

          tab33.cells[j].innerHTML = moyuet; //listStudent[i][9][3]
        }

        ;

        if (j == 3) {
          tab33.cells[j].innerHTML = uef910cr;
        }
      } //tab4


      tab4 = temp.children[4];
      tab41 = tab4.children.nested333;
      tab42 = tab41.children['0'];
      tab43 = tab42.children['0'];

      for (j = 0; j <= tab43.childElementCount - 1; j++) {
        if (j == 0) {
          tab43.cells[j].innerHTML = listStudent[i][11][1];
        }

        ;

        if (j == 1) {
          tab43.cells[j].innerHTML = listStudent[i][11][2];
        }

        ;
        ;

        if (j == 2) {
          tab43.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][11][2]) + 1;
        } //listStudent[i][2][7] + listStudent[i][4][7] + listStudent[i][5][7] + listStudent[i][6][7] + listStudent[i][7][7] + listStudent[i][8][7] + listStudent[i][9][7] + listStudent[i][10][7] };


        if (j == 3) {
          tab43.cells[j].innerHTML = listStudent[i][11][3];
        } //'/' /*mydata[2].indexOf(listStudent[i][11][2]) + 1*/ }


        if (j == 4) {
          tab43.cells[j].innerHTML = '/';
        }

        ;
      } //Ajoute de la ligne au grand tableau


      worktab.appendChild(temp);
      body.appendChild(page0);
    }
  }

  Page1();

  function PageRattrapage() {
    listStudent = mydata[1];
    rattrapage = mydata[8];
    page1 = document.getElementById('page');
    page1 = page1.cloneNode(true); //Changement Title

    page1.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE SYNTHESE 1<sup>er</sup> SEMESTRE MDS2  ".concat(mydata[9][0]['annee_academique']);
    bigtab1 = page1.children[0].children[2].children[1]; //Tableau Sur lequel on ajoute les nouvelles lignes

    worktab1 = bigtab1.children[1];
    worktab1.children[0].children[0].innerHTML = "PROCES VERBAL MODULAIRE MDS2 ".concat(mydata[9][0]['annee_academique']);

    for (i = 0; i <= mydata[1].length - 1; i++) {
      temp1 = worktab1.children[3].cloneNode(true); //tab0 NOMS ET INFOS ETUDIANTS

      tab0 = temp1.children[0];
      tab01 = tab0.children.nested4;
      tab02 = tab01.children;
      tab03 = tab02['0'];
      tab04 = tab03.children;
      tab05 = tab04[0]; //good  

      for (j = 0; j <= tab05.childElementCount - 1; j++) {
        if (j == 0) {
          tab05.cells[j].innerHTML = i + 1; //tab005.cells[j].innerHTML = i + 1;
        }

        if (j == 1) {
          tab05.cells[j].innerHTML = listStudent[i][0]['nom']; //tab005.cells[j].innerHTML = listStudent[i][0]['nom'];
        }

        if (j == 2) {
          tab05.cells[j].innerHTML = listStudent[i][0]['prenom']; //tab005.cells[j].innerHTML = listStudent[i][0]['prenom']
        }

        if (j == 3) {
          tab05.cells[j].innerHTML = listStudent[i][0]['matricule']; //tab005.cells[j].innerHTML = listStudent[i][0]['matricule']
          //tab005.cells[j].innerHTML = listStudent[i][0]['date_naissance']
        }
      } //tab1 UE FONDAMENTALES


      tab1 = temp1.children[1];
      tab11 = tab1.children.nested11;
      tab12 = tab11.children;
      tab13 = tab12['0'];
      tab14 = tab13.children;
      tab15 = tab14[0]; //good line

      for (j = 0; j <= tab15.childElementCount - 1; j++) {
        if (j == 0) {
          ue1r = sommeFloat2(0.7 * rattrapage[i][1], 0.3 * listStudent[i][1][8]);

          if (rattrapage[i][1] == 0) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = ue1r;
          }
        }

        if (j == 1) {
          ue2r = sommeFloat2(0.7 * rattrapage[i][2], 0.3 * listStudent[i][2][8]);

          if (rattrapage[i][2] == 0) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = ue2r;
          }
        }

        if (j == 2) {
          /*var uef1cr = listStudent[i][1][6]
          if (listStudent[i][1][0] < 10) { uef1cr = 0 } 
            var uef2cr = listStudent[i][2][6]
          if (listStudent[i][2][0] < 10) { uef2cr = 0 } 
            moyuef = listStudent[i][1][3]
            if (moyuef >= 10 && (listStudent[i][1][0] >= 7 && listStudent[i][2][0] >= 7)) {
              moyuefcr = listStudent[i][1][6] + listStudent[i][2][6]
          } else {
              moyuef = '--'
              moyuefcr = uef1cr + uef2cr
          }*/
          ue3r = sommeFloat2(0.7 * rattrapage[i][3], 0.3 * listStudent[i][3][8]);

          if (rattrapage[i][3] == 0) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = ue3r;
          }
        }

        if (j == 3) {
          ue4r = sommeFloat2(0.7 * rattrapage[i][4], 0.3 * listStudent[i][4][8]);

          if (rattrapage[i][4] == 0) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = ue4r;
          }
        }

        if (j == 4) {
          /*if (rattrapage[i][4] == 0) {*/
          tab15.cells[j].innerHTML = '--';
          /*} else { tab15.cells[j].innerHTML = rattrapage[i][4]; }*/
        }

        if (j == 5) {
          var ue1 = listStudent[i][1][6];

          if (ue1r < 10) {
            ue1 = 0;
          }

          var ue2 = listStudent[i][2][6];

          if (ue2r < 10) {
            ue2 = 0;
          }

          var ue3 = listStudent[i][3][6];

          if (ue3r < 10) {
            ue3 = 0;
          }

          var ue4 = listStudent[i][4][6];

          if (ue4r < 10) {
            ue4 = 0;
          }

          ue12 = 0;
          ue34 = 0;

          if (ue1r > 10 || ue2r > 10) {
            ue12 = listStudent[i][1][6];
          }

          if (ue3r > 10 || ue4r > 10) {
            ue34 = listStudent[i][3][6];
          }
          /*if ((ue4r + ue3r) < 20) { ue4 = 0 } else {}
          if ((ue4r + ue3r) < 20) { ue4 = 0 } else {}*/


          tab15.cells[j].innerHTML = ue12 + ue34;
        }
      } //tab2 UE PROFESSIONNELLES


      tab2 = temp1.children[2];
      tab21 = tab2.children.nested22;
      tab22 = tab21.children['0'];
      tab23 = tab22.children['0'];

      for (j = 0; j <= tab23.childElementCount - 1; j++) {
        if (j == 0) {
          ue5r = sommeFloat2(0.7 * rattrapage[i][5], 0.3 * listStudent[i][5][8]);

          if (rattrapage[i][5] == 0) {
            tab23.cells[j].innerHTML = '--';
          } else {
            tab23.cells[j].innerHTML = ue5r;
          }
        }

        ;

        if (j == 1) {
          ue6r = sommeFloat2(0.7 * rattrapage[i][6], 0.3 * listStudent[i][6][8]);

          if (rattrapage[i][6] == 0) {
            tab23.cells[j].innerHTML = '--';
          } else {
            tab23.cells[j].innerHTML = ue6r;
          }
        }

        ;

        if (j == 2) {
          ue7r = sommeFloat2(0.7 * rattrapage[i][7], 0.3 * listStudent[i][7][8]);

          if (rattrapage[i][7] == 0) {
            tab23.cells[j].innerHTML = '--';
          } else {
            tab23.cells[j].innerHTML = ue7r;
          }
        }

        ;

        if (j == 3) {
          ue8r = sommeFloat2(0.7 * rattrapage[i][8], 0.3 * listStudent[i][8][8]);

          if (rattrapage[i][8] == 0) {
            tab23.cells[j].innerHTML = '--';
          } else {
            tab23.cells[j].innerHTML = ue8r;
          }
        }

        ;

        if (j == 4) {
          tab23.cells[j].innerHTML = '--';
          /*listStudent[i][7][0]*/
        }

        ;

        if (j == 5) {
          var ue5 = listStudent[i][5][6];

          if (ue5r < 10) {
            ue5 = 0;
          }

          var ue6 = listStudent[i][6][6];

          if (ue6r < 10) {
            ue6 = 0;
          }

          var ue7 = listStudent[i][7][6];

          if (ue7r < 10) {
            ue7 = 0;
          }

          var ue8 = listStudent[i][8][6];

          if (ue8r < 10) {
            ue8 = 0;
          }

          ue56 = 0;
          ue78 = 0;

          if (ue5r > 10 || ue6r > 10) {
            ue56 = listStudent[i][5][6];
          }

          if (ue7r > 10 || ue8r > 10) {
            ue78 = listStudent[i][7][6];
          }

          tab23.cells[j].innerHTML = ue56 + ue78;
          /*listStudent[i][8][0]*/
        }

        ;
      } //tab3 UE TRANSVERSALES


      tab3 = temp1.children[3];
      tab31 = tab3.children.nested33;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        if (j == 0) {
          ue9r = sommeFloat2(0.7 * rattrapage[i][9], 0.3 * listStudent[i][9][8]);

          if (rattrapage[i][9] == 0) {
            tab33.cells[j].innerHTML = '--';
          } else {
            tab33.cells[j].innerHTML = ue9r;
          }
        }

        ;

        if (j == 1) {
          ue10r = sommeFloat2(0.7 * rattrapage[i][10], 0.3 * listStudent[i][10][8]);

          if (rattrapage[i][10] == 0) {
            tab33.cells[j].innerHTML = '--';
          } else {
            tab33.cells[j].innerHTML = ue10r;
          }
        }

        ;

        if (j == 2) {
          tab33.cells[j].innerHTML = "--";
          /*Moyenne Groupe*/
        }

        ;

        if (j == 3) {
          var ue9 = listStudent[i][9][6];

          if (ue9r < 10) {
            ue9 = 0;
          }

          var ue10 = listStudent[i][10][6];

          if (ue10r < 10) {
            ue10 = 0;
          }

          tab33.cells[j].innerHTML = ue9 + ue10; //Crédits
        }

        ;
      } //RESULTATS


      tab44 = temp1.children[4];
      tab441 = tab44.children.nested333;
      tab442 = tab441.children['0'];
      tab443 = tab442.children['0'];

      for (j = 0; j <= tab443.childElementCount - 1; j++) {
        if (j == 0) {
          tab443.cells[j].innerHTML = '--';
        } //total }


        if (j == 1) {
          tab443.cells[j].innerHTML = '--';
          ;
        } //moyenne }


        if (j == 2) {
          tab443.cells[j].innerHTML = '--';
        } //moyuefcr + moyuepcr + moyuetcr


        if (j == 3) {
          tab443.cells[j].innerHTML = '--';
        } //rang }


        if (j == 4) {
          tab443.cells[j].innerHTML = "--";
        }
      } //Ajoute de la ligne au grand tableau


      worktab1.appendChild(temp1);
      body.appendChild(page1);
    }
  } //PageRattrapage()


  function PageSynthese() {
    synthese = mydata[9];
    var page2 = document.getElementById('page');
    page2 = page2.cloneNode(true); //Changement Title

    page2.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE SYNTHESE 1<sup>er</sup> SEMESTRE MDS2  ".concat(mydata[9][0]['annee_academique']);
    bigtab2 = page2.children[0].children[2].children[1]; //Tableau Sur lequel on ajoute les nouvelles lignes

    worktab2 = bigtab2.children[1];
    worktab2.children[0].children[0].innerHTML = "PROCES VERBAL MODULAIRE MDS2 ".concat(mydata[9][0]['annee_academique']);

    for (i = 0; i <= mydata[1].length - 1; i++) {
      temp2 = worktab2.children[3].cloneNode(true); //tab0 NOMS ET INFOS ETUDIANTS

      tab0 = temp2.children[0];
      tab01 = tab0.children.nested4;
      tab02 = tab01.children;
      tab03 = tab02['0'];
      tab04 = tab03.children;
      tab05 = tab04[0]; //good  

      for (j = 0; j <= tab05.childElementCount - 1; j++) {
        if (j == 0) {
          tab05.cells[j].innerHTML = i + 1; //tab005.cells[j].innerHTML = i + 1;
        }

        if (j == 1) {
          tab05.cells[j].innerHTML = listStudent[i][0]['nom']; //tab005.cells[j].innerHTML = listStudent[i][0]['nom'];
        }

        if (j == 2) {
          tab05.cells[j].innerHTML = listStudent[i][0]['prenom']; //tab005.cells[j].innerHTML = listStudent[i][0]['prenom']
        }

        if (j == 3) {
          tab05.cells[j].innerHTML = listStudent[i][0]['matricule']; //tab005.cells[j].innerHTML = listStudent[i][0]['matricule']
          //tab005.cells[j].innerHTML = listStudent[i][0]['date_naissance']
        }
      } //tab1 UE FONDAMENTALES


      tab1 = temp2.children[1];
      tab11 = tab1.children.nested11;
      tab12 = tab11.children;
      tab13 = tab12['0'];
      tab14 = tab13.children;
      tab15 = tab14[0]; //good line

      for (j = 0; j <= tab15.childElementCount - 1; j++) {
        if (j == 0) {
          tab15.cells[j].innerHTML = synthese[i][1][0];
        }

        ;

        if (j == 1) {
          tab15.cells[j].innerHTML = synthese[i][2][0];
        }

        if (j == 2) {
          tab15.cells[j].innerHTML = synthese[i][3][0];
        }

        if (j == 3) {
          tab15.cells[j].innerHTML = synthese[i][4][0];
        }

        if (j == 4) {
          var uef12cr = synthese[i][1][5]; //synthese[i][1][6]
          //if ((synthese[i][1][0] + synthese[i][2][0]) < 20) { uef12cr = 0 }

          /*var uef2cr = listStudent[i][2][6]
          if (listStudent[i][2][0] < 10) { uef2cr = 0 }*/

          var uef34cr = synthese[i][3][5]; //synthese[i][3][6]
          //if ((synthese[i][3][0] + synthese[i][4][0]) < 20) { uef34cr = 0 }

          /*var uef2cr = listStudent[i][4][6]
          if (listStudent[i][4][0] < 10) { uef2cr = 0 }*/

          moyuef = synthese[i][1][3];

          if (moyuef >= 10 && synthese[i][1][0] >= 7 && synthese[i][2][0] >= 7 && synthese[i][3][0] >= 7 && synthese[i][4][0] >= 7) {
            moyuefcr = uef34cr + uef12cr;
          } else {
            moyuef = '--'; //moyuefcr = uef1cr + uef2cr
          }

          tab15.cells[j].innerHTML = moyuef; //listStudent[i][1][3];
        }

        if (j == 5) {
          tab15.cells[j].innerHTML = uef12cr + uef34cr;
        }
      } //tab2 UE PROFESSIONNELLES


      tab2 = temp2.children[2];
      tab21 = tab2.children.nested22;
      tab22 = tab21.children['0'];
      tab23 = tab22.children['0'];

      for (j = 0; j <= tab23.childElementCount - 1; j++) {
        if (j == 0) {
          ue5r = synthese[i][5][0]; //sommeFloat2(0.7 * rattrapage[i][5], 0.3 * listStudent[i][5][8])

          tab23.cells[j].innerHTML = synthese[i][5][0]; //if (rattrapage[i][5] == 0) { tab23.cells[j].innerHTML = '--' } else { tab23.cells[j].innerHTML = ue5r; }
        }

        ;

        if (j == 1) {
          ue6r = synthese[i][6][0]; //sommeFloat2(0.7 * rattrapage[i][6], 0.3 * listStudent[i][6][8])

          tab23.cells[j].innerHTML = synthese[i][6][0]; //if (rattrapage[i][6] == 0) { tab23.cells[j].innerHTML = '--' } else { tab23.cells[j].innerHTML = ue6r; }
        }

        ;

        if (j == 2) {
          ue7r = synthese[i][7][0]; //sommeFloat2(0.7 * rattrapage[i][7], 0.3 * listStudent[i][7][8])

          tab23.cells[j].innerHTML = synthese[i][7][0]; //if (rattrapage[i][7] == 0) { tab23.cells[j].innerHTML = '--' } else { tab23.cells[j].innerHTML = ue7r; }
        }

        ;

        if (j == 3) {
          ue8r = synthese[i][8][0]; //sommeFloat2(0.7 * rattrapage[i][8], 0.3 * listStudent[i][8][8])

          tab23.cells[j].innerHTML = synthese[i][8][0]; //if (rattrapage[i][8] == 0) { tab23.cells[j].innerHTML = '--' } else { tab23.cells[j].innerHTML = ue8r; }
        }

        ;

        if (j == 4) {
          var uef5cr = synthese[i][5][5]; //if ((synthese[i][5][0]) < 10) { uef5cr = 0 }

          var uef6cr = synthese[i][6][5]; //if ((synthese[i][6][0]) < 10) { uef6cr = 0 }

          var uef7cr = synthese[i][7][5]; //if ((synthese[i][7][0]) < 10) { uef7cr = 0 }

          var uef8cr = synthese[i][8][5]; //if ((listStudent[i][8][0]) < 10) { uef8cr = 0 }

          var moyuefcr = uef5cr + uef6cr + uef7cr + uef8cr;
          moyuep = synthese[i][5][3];

          if (moyuep >= 10 && synthese[i][5][0] >= 7 && synthese[i][6][0] >= 7 && synthese[i][7][0] >= 7 && synthese[i][8][0] >= 7) {//moyuefcr = uef56cr + uef78cr
          } else {
            moyuep = '--'; //moyuefcr = uef1cr + uef2cr
          }

          tab23.cells[j].innerHTML = moyuep;
        }

        ;

        if (j == 5) {
          tab23.cells[j].innerHTML = moyuefcr; //ue5678 /*listStudent[i][8][0]*/
        }

        ;
      } //tab3 UE TRANSVERSALES


      tab3 = temp2.children[3];
      tab31 = tab3.children.nested33;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        ue910 = 0;

        if (j == 0) {
          ue9r = synthese[i][9][0]; //sommeFloat2(0.7 * rattrapage[i][9], 0.3 * listStudent[i][9][8])

          /*if (ue9r < 10) { tab33.cells[j].innerHTML = '--' } else {*/

          tab33.cells[j].innerHTML = ue9r; //}
        }

        ;

        if (j == 1) {
          ue10r = synthese[i][10][0]; //sommeFloat2(0.7 * rattrapage[i][10], 0.3 * listStudent[i][10][8])

          /*if (ue10r < 10) { tab33.cells[j].innerHTML = '--' } else {*/

          tab33.cells[j].innerHTML = ue10r; //}
        }

        ;

        if (j == 2) {
          var uef9cr = synthese[i][9][5]; //if ((listStudent[i][9][0]) < 10) { uef9cr = 0 }

          var uef10cr = synthese[i][10][5]; //if ((listStudent[i][10][0]) < 10) { uef10cr = 0 }

          var uef910cr = uef9cr + uef10cr;
          moyuet = synthese[i][9][3];

          if (moyuet >= 10 && synthese[i][9][0] >= 7 && synthese[i][10][0] >= 7) {//uef910cr = uef9cr + uef10cr
          } else {
            moyuet = '--'; //moyuefcr = uef1cr + uef2cr
          }

          tab33.cells[j].innerHTML = moyuet;
          /*Moyenne Groupe*/
        }

        ;

        if (j == 3) {
          /*var ue910 = 0
          var ue9 = listStudent[i][9][6]
          if (ue9r < 10) { ue9 = 0 }
            var ue10 = listStudent[i][10][6]
          if ((ue10r) < 10) { ue10 = 0 }
            if ((ue9r + ue10r) >= 20) { ue910 = listStudent[i][9][6] + listStudent[i][10][6] } else { ue910 = ue9 + ue10 }*/
          tab33.cells[j].innerHTML = uef910cr; //Crédits
        }

        ;
      } //RESULTATS


      tab44 = temp2.children[4];
      tab441 = tab44.children.nested333;
      tab442 = tab441.children['0'];
      tab443 = tab442.children['0'];

      for (j = 0; j <= tab443.childElementCount - 1; j++) {
        if (j == 0) {
          tab443.cells[j].innerHTML = synthese[i][11][1];
        } //total }


        if (j == 1) {
          /* if ((synthese[i][1][3] + synthese[i][5][3] + synthese[i][9][3]) >= 30)*/
          tab443.cells[j].innerHTML = synthese[i][11][2];
          /*} else { tab443.cells[j].innerHTML = '--' } //moyenne }*/
        }

        if (j == 2) {
          tab443.cells[j].innerHTML = '/';
        } //moyuefcr + moyuepcr + moyuetcr


        if (j == 3) {
          tab443.cells[j].innerHTML = synthese[i][11][3]
          /*'/'*/
          ;
        } //rang }


        if (j == 4) {
          tab443.cells[j].innerHTML = "/";
        }
      } //Ajoute de la ligne au grand tableau


      worktab2.appendChild(temp2);
      body.appendChild(page2);
    }
  } //PageSynthese()

  /**FUNCTION MULTI_PAGE FOR PROCES VERBAL */


  function ListProcess() {
    body = document.getElementById('body');
    page = document.getElementById('page2');
    listProces = document.createElement('div');

    for (i = 0; i <= 9; i++) {
      clone = page.cloneNode(true);
      clone.style.display = 'block';
      clone = fullfill(clone, i);
      listProces.appendChild(clone);
    } //Fixation de ListProcess sur le body de la page


    body.appendChild(listProces);
  }
  /**FONCTION DE REMPLISSAGE DU CLONE */


  function fullfill(clone, i) {
    //Pagination
    pagination = clone.children[3]; //Line 1

    line1 = clone.children[1].children[0].children[1].innerHTML = "Edition du : ".concat(mydata[4]); //Line 2

    line2 = clone.children[1].children[1].children[0];
    line2.children[2].innerHTML = ' MANAGEMENT DU SPORT';
    line2.children[5].innerHTML = "".concat(mydata[9][0]['annee_academique']); //Third Line

    line3 = clone.children[1].children[2].children[0];

    if (i == 0) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS111"; //

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"MATHEMATIQUES I";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][0]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 1) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS111";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"INFORMATIQUE I";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][1]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 2) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS112";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"MATHEMATIQUES FINANCIERES";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][2]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 3) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS112";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"STATISTIQUES DESCRIPTIVES";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][3]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 4) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS113";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"ENVIRONNEMENT JURIDIQUE ET COMPTABLE I";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][4]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 5) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; // "MDS114";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"MARKETING";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][5]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 6) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS115";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"OUTILS DE GESTION DU SPORT I";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][6]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 7) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; //"MDS116";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"GESTION DES STRUCTURES ET ORGANISATIONS SPORTIVES I";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][7]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 8) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; // "MDS117";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"TECHNIQUE D'EXPRESSION ANGLAISE";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][8]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    }

    if (i == 9) {
      line3.children[1].innerHTML = mydata[8][i]['code_UE']; // "MDS117";

      line3.children[2].innerHTML = mydata[8][i]['intitule_UE']; //"TECHNIQUE D'EXPRESSION FRANCAISE";

      line3.children[4].innerHTML = mydata[8][i]['nombre_credit']; //mydata[5][9]

      line3.children[6].innerHTML = mydata[8][i]['semestre_id']; //'1'

      pagination.innerText = "Page ".concat(i + 1, " / ").concat(mydata[5].length - 1);
    } //Tableau des students


    tab = clone.children[2].children[0]; //Car pas encore de notes de rattrapage donc pas de SYNTHESE
    //listStudent = mydata[9] //mydata[1]

    listStudent = mydata[1];
    tableContainer = document.getElementById('tableContainer');
    /**STATS */

    for (j = 0; j <= mydata[1].length - 1; j++) {
      line = document.createElement('tr');

      for (k = 0; k <= 8; k++) {
        td = document.createElement('td');

        if (k == 0) {
          td.innerHTML = "".concat(j + 1);
          td.setAttribute('class', 'numero');
        }

        if (k == 1) {
          td.innerHTML = "".concat(listStudent[j][0]['matricule']);
          td.setAttribute('class', 'matricule');
        }

        if (k == 2) {
          td.innerHTML = "".concat(listStudent[j][0]['nom']) + " ".concat(listStudent[j][0]['prenom']);
          td.setAttribute('class', 'nomprenon');
        }

        if (k == 3) {
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][8]);
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][8]);
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][8]);
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][8]);
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][8]);
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][8]);
          }

          if (i == 6) {
            td.innerHTML = "".concat(listStudent[j][7][8]);
          }

          if (i == 7) {
            td.innerHTML = "".concat(listStudent[j][8][8]);
          }

          if (i == 8) {
            td.innerHTML = "".concat(listStudent[j][9][8]);
          }

          if (i == 9) {
            td.innerHTML = "".concat(listStudent[j][10][8]);
          }

          td.setAttribute('class', 'cc');
        }

        if (k == 4) {
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][9]);
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][9]);
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][9]);
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][9]);
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][9]);
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][9]);
          }

          if (i == 6) {
            td.innerHTML = "".concat(listStudent[j][7][9]);
          }

          if (i == 7) {
            td.innerHTML = "".concat(listStudent[j][8][9]);
          }

          if (i == 8) {
            td.innerHTML = "".concat(listStudent[j][9][9]);
          }

          if (i == 9) {
            td.innerHTML = "".concat(listStudent[j][10][9]);
          }
        }

        if (k == 5) {
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][0]);
            td.setAttribute('class', 'moyenne');
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][0]);
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][0]);
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][0]);
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][0]);
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][0]);
          }

          if (i == 6) {
            td.innerHTML = "".concat(listStudent[j][7][0]);
          }

          if (i == 7) {
            td.innerHTML = "".concat(listStudent[j][8][0]);
          }

          if (i == 8) {
            td.innerHTML = "".concat(listStudent[j][9][0]);
          }

          if (i == 9) {
            td.innerHTML = "".concat(listStudent[j][10][0]);
          }
        }

        if (k == 6) {
          if (i == 0) {
            if (listStudent[j][1][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][1][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 1) {
            if (listStudent[j][2][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][2][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 2) {
            if (listStudent[j][3][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][3][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 3) {
            if (listStudent[j][4][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][4][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 4) {
            if (listStudent[j][5][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][5][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 5) {
            if (listStudent[j][6][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][6][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 6) {
            if (listStudent[j][7][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][7][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 7) {
            if (listStudent[j][8][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][8][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 8) {
            if (listStudent[j][9][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][9][6]);
            } else {
              td.innerHTML = 0;
            }
          }

          if (i == 9) {
            if (listStudent[j][10][0] >= 10) {
              td.innerHTML = "".concat(listStudent[j][10][6]);
            } else {
              td.innerHTML = 0;
            }
          }
        }

        if (k == 7) {
          if (i == 0) {
            if (listStudent[j][1][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 1) {
            if (listStudent[j][2][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 2) {
            if (listStudent[j][3][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 3) {
            if (listStudent[j][4][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 4) {
            if (listStudent[j][5][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 5) {
            if (listStudent[j][6][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 6) {
            if (listStudent[j][7][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 7) {
            if (listStudent[j][8][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 8) {
            if (listStudent[j][9][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }

          if (i == 9) {
            if (listStudent[j][10][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }
          }
        }

        if (k == 8) {
          if (i == 0) {
            if (listStudent[j][1][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][1][0] >= 15 && listStudent[j][1][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][1][0] >= 14 && listStudent[j][1][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][1][0] >= 13 && listStudent[j][1][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][1][0] >= 12 && listStudent[j][1][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][1][0] >= 11 && listStudent[j][1][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][1][0] >= 10 && listStudent[j][1][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][1][0] >= 9 && listStudent[j][1][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][1][0] >= 8 && listStudent[j][1][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][1][0] >= 7 && listStudent[j][1][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][1][0] >= 6 && listStudent[j][1][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][1][0] >= 0 && listStudent[j][1][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 1) {
            if (listStudent[j][2][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][2][0] >= 15 && listStudent[j][2][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][2][0] >= 14 && listStudent[j][2][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][2][0] >= 13 && listStudent[j][2][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][2][0] >= 12 && listStudent[j][2][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][2][0] >= 11 && listStudent[j][2][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][2][0] >= 10 && listStudent[j][2][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][2][0] >= 9 && listStudent[j][2][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][2][0] >= 8 && listStudent[j][2][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][2][0] >= 7 && listStudent[j][2][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][2][0] >= 6 && listStudent[j][2][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][2][0] >= 0 && listStudent[j][2][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 2) {
            if (listStudent[j][3][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][3][0] >= 15 && listStudent[j][3][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][3][0] >= 14 && listStudent[j][3][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][3][0] >= 13 && listStudent[j][3][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][3][0] >= 12 && listStudent[j][3][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][3][0] >= 11 && listStudent[j][3][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][3][0] >= 10 && listStudent[j][3][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][3][0] >= 9 && listStudent[j][3][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][3][0] >= 8 && listStudent[j][3][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][3][0] >= 7 && listStudent[j][3][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][3][0] >= 6 && listStudent[j][3][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][3][0] >= 0 && listStudent[j][3][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 3) {
            if (listStudent[j][4][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][4][0] >= 15 && listStudent[j][4][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][4][0] >= 14 && listStudent[j][4][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][4][0] >= 13 && listStudent[j][4][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][4][0] >= 12 && listStudent[j][4][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][4][0] >= 11 && listStudent[j][4][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][4][0] >= 10 && listStudent[j][4][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][4][0] >= 9 && listStudent[j][4][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][4][0] >= 8 && listStudent[j][4][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][4][0] >= 7 && listStudent[j][4][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][4][0] >= 6 && listStudent[j][4][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][4][0] >= 0 && listStudent[j][4][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 4) {
            if (listStudent[j][5][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][5][0] >= 15 && listStudent[j][5][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][5][0] >= 14 && listStudent[j][5][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][5][0] >= 13 && listStudent[j][5][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][5][0] >= 12 && listStudent[j][5][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][5][0] >= 11 && listStudent[j][5][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][5][0] >= 10 && listStudent[j][5][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][5][0] >= 9 && listStudent[j][5][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][5][0] >= 8 && listStudent[j][5][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][5][0] >= 7 && listStudent[j][5][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][5][0] >= 6 && listStudent[j][5][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][5][0] >= 0 && listStudent[j][5][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 5) {
            if (listStudent[j][6][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][6][0] >= 15 && listStudent[j][6][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][6][0] >= 14 && listStudent[j][6][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][6][0] >= 13 && listStudent[j][6][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][6][0] >= 12 && listStudent[j][6][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][6][0] >= 11 && listStudent[j][6][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][6][0] >= 10 && listStudent[j][6][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][6][0] >= 9 && listStudent[j][6][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][6][0] >= 8 && listStudent[j][6][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][6][0] >= 7 && listStudent[j][6][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][6][0] >= 6 && listStudent[j][6][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][6][0] >= 0 && listStudent[j][6][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 6) {
            if (listStudent[j][7][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][7][0] >= 15 && listStudent[j][7][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][7][0] >= 14 && listStudent[j][7][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][7][0] >= 13 && listStudent[j][7][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][7][0] >= 12 && listStudent[j][7][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][7][0] >= 11 && listStudent[j][7][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][7][0] >= 10 && listStudent[j][7][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][7][0] >= 9 && listStudent[j][7][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][7][0] >= 8 && listStudent[j][7][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][7][0] >= 7 && listStudent[j][7][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][7][0] >= 6 && listStudent[j][7][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][7][0] >= 0 && listStudent[j][7][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 7) {
            if (listStudent[j][8][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][8][0] >= 15 && listStudent[j][8][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][8][0] >= 14 && listStudent[j][8][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][8][0] >= 13 && listStudent[j][8][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][8][0] >= 12 && listStudent[j][8][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][8][0] >= 11 && listStudent[j][8][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][8][0] >= 10 && listStudent[j][8][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][8][0] >= 9 && listStudent[j][8][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][8][0] >= 8 && listStudent[j][8][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][8][0] >= 7 && listStudent[j][8][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][8][0] >= 6 && listStudent[j][8][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][8][0] >= 0 && listStudent[j][8][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 8) {
            if (listStudent[j][9][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][9][0] >= 15 && listStudent[j][9][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][9][0] >= 14 && listStudent[j][9][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][9][0] >= 13 && listStudent[j][9][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][9][0] >= 12 && listStudent[j][9][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][9][0] >= 11 && listStudent[j][9][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][9][0] >= 10 && listStudent[j][9][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][9][0] >= 9 && listStudent[j][9][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][9][0] >= 8 && listStudent[j][9][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][9][0] >= 7 && listStudent[j][9][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][9][0] >= 6 && listStudent[j][9][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][9][0] >= 0 && listStudent[j][9][0] < 6) {
              td.innerHTML = 'F';
            }
          }

          if (i == 9) {
            if (listStudent[j][10][0] >= 16) {
              td.innerHTML = 'A';
            } else if (listStudent[j][10][0] >= 15 && listStudent[j][10][0] < 16) {
              td.innerHTML = 'A-';
            } else if (listStudent[j][10][0] >= 14 && listStudent[j][10][0] < 15) {
              td.innerHTML = 'B+';
            } else if (listStudent[j][10][0] >= 13 && listStudent[j][10][0] < 14) {
              td.innerHTML = 'B';
            } else if (listStudent[j][10][0] >= 12 && listStudent[j][10][0] < 13) {
              td.innerHTML = 'B-';
            } else if (listStudent[j][10][0] >= 11 && listStudent[j][10][0] < 12) {
              td.innerHTML = 'C+';
            } else if (listStudent[j][10][0] >= 10 && listStudent[j][10][0] < 11) {
              td.innerHTML = 'C';
            } else if (listStudent[j][10][0] >= 9 && listStudent[j][10][0] < 10) {
              td.innerHTML = 'C-';
            } else if (listStudent[j][10][0] >= 8 && listStudent[j][10][0] < 9) {
              td.innerHTML = 'D+';
            } else if (listStudent[j][10][0] >= 7 && listStudent[j][10][0] < 8) {
              td.innerHTML = 'D';
            } else if (listStudent[j][10][0] >= 6 && listStudent[j][10][0] < 7) {
              td.innerHTML = 'E';
            } else if (listStudent[j][10][0] >= 0 && listStudent[j][10][0] < 6) {
              td.innerHTML = 'F';
            }
          }
        }

        line.appendChild(td);
      }

      tab.children[1].appendChild(line);
    } //Tableau des stats


    tabstat = clone.children[2].children[1];
    ligneStat1 = tabstat.children[0].children[1].children[0];
    ligneStat1.children[1];
    ligneStat1.children[2];
    ligneStat1.children[3];
    ligneStat1.children[4];
    ligneStat2 = tabstat.children[0].children[1].children[1];
    ligneStat3 = tabstat.children[0].children[1].children[2];
    ligneStat4 = tabstat.children[0].children[1].children[3];

    if (i == 0) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][0]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][0]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][0]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][0]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][0]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][0]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][0]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][0]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][0]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][0]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][0]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][0]['pourcentageTB'], " %");
    }

    if (i == 1) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][1]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][1]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][1]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][1]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][1]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][1]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][1]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][1]['pourcentage'])
      /*(100-(mydata[6][1]['pourcentage']))*/
      , " %");
      ligneStat3.children[4].innerHTML = mydata[7][1]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][1]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][1]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][1]['pourcentageTB'], " %");
    }

    if (i == 2) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][2]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][2]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][2]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][2]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][2]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][2]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][2]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][2]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][2]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][2]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][2]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][2]['pourcentageTB'], " %");
    }

    if (i == 3) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][3]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][3]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][3]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][3]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][3]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][3]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][3]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][3]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][3]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][3]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][3]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][3]['pourcentageTB'], " %");
    }

    if (i == 4) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][4]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][4]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][4]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][4]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][4]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][4]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][4]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][4]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][4]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][4]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][4]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][4]['pourcentageTB'], " %");
    }

    if (i == 5) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][5]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][5]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][5]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][5]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][5]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][5]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][5]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][5]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][5]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][5]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][5]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][5]['pourcentageTB'], " %");
    }

    if (i == 6) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][6]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][6]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][6]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][6]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][6]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][6]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][6]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][6]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][6]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][6]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][6]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][6]['pourcentageTB'], " %");
    }

    if (i == 7) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][7]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][7]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][7]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][7]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][7]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][7]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][7]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][7]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][7]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][7]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][7]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][7]['pourcentageTB'], " %");
    }

    if (i == 8) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][8]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][8]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][8]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][8]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][8]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][8]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][8]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][8]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][8]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][8]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][8]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][8]['pourcentageTB'], " %");
    }

    if (i == 9) {
      //Ligne 1
      ligneStat1.children[1].innerHTML = mydata[1].length;
      ligneStat1.children[4].innerHTML = mydata[7][9]['Passable'];
      ligneStat1.children[5].innerHTML = "".concat(mydata[7][9]['pourcentageP'], " %"); //Ligne2

      ligneStat2.children[1].innerHTML = mydata[6][9]['nombre'];
      ligneStat2.children[2].innerHTML = "".concat(mydata[6][9]['pourcentage'], " %");
      ligneStat2.children[4].innerHTML = mydata[7][9]['Assez Bien'];
      ligneStat2.children[5].innerHTML = "".concat(mydata[7][9]['pourcentageAB'], " %"); //Ligne3

      ligneStat3.children[1].innerHTML = mydata[1].length - mydata[6][9]['nombre'];
      ligneStat3.children[2].innerHTML = "".concat(floatfix(mydata[6][9]['pourcentage']), " %");
      ligneStat3.children[4].innerHTML = mydata[7][9]['Bien'];
      ligneStat3.children[5].innerHTML = "".concat(mydata[7][9]['pourcentageB'], " %"); //Ligne4

      ligneStat4.children[4].innerHTML = mydata[7][9]['Très Bien'];
      ligneStat4.children[5].innerHTML = "".concat(mydata[7][9]['pourcentageTB'], " %");
    }

    return clone;
  }

  ListProcess();
});

function floatfix(a) {
  return (100 - a).toFixed(2);
}

function sommeFloat2(a, b) {
  /*a = parseFloat(a)
  b = parseFloat(b);*/
  result = a + b;
  result = result.toFixed(2);
  return result;
}