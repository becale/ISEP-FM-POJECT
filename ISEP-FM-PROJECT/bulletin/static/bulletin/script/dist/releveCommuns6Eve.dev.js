"use strict";

window.addEventListener('load', function () {
  //Recuperation de la variable des données
  mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
  console.log(mydata);

  function Page1() {
    listStudent = mydata[1];
    page1 = document.getElementById('page');
    page1 = page1.cloneNode(true);
    bigtab = page1.children[0].children[2].children[1]; //Tableau Sur lequel on ajoute les nouvelles lignes

    worktab = bigtab.children[1]; //Ligne des 4 Tableaux

    for (i = 0; i <= mydata[1].length - 1; i++) {
      temp = worktab.children[3].cloneNode(true); //tab0

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
      } //tab1


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
          var uef11cr = listStudent[i][1][6];

          if (listStudent[i][1][0] < 10) {
            uef11cr = 0;
          }

          var uef22cr = listStudent[i][2][6];

          if (listStudent[i][2][0] < 10) {
            uef22cr = 0;
          }

          var uef33cr = listStudent[i][3][6];

          if (listStudent[i][3][0] < 10) {
            uef33cr = 0;
          }

          var uef44cr = listStudent[i][4][6];

          if (listStudent[i][4][0] < 10) {
            uef44cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (listStudent[i][1][0] + listStudent[i][2][0] + listStudent[i][3][0] + listStudent[i][4][0] >= 40) {
            uef1234cr1 = listStudent[i][1][6] + listStudent[i][2][6] + listStudent[i][3][6] + listStudent[i][4][6];
          } else {
            uef1234cr1 = uef11cr + uef22cr + uef33cr + uef44cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyuef1 = listStudent[i][1][3];

          if (moyuef1 >= 10 && listStudent[i][1][0] >= 7 && listStudent[i][2][0] >= 7 && listStudent[i][3][0] >= 7 && listStudent[i][4][0] >= 7) {//moyuefcr = uef34cr + uef12cr
          } else {
            moyuef1 = '--';
          }

          tab15.cells[j].innerHTML = moyuef1;
        }

        if (j == 5) {
          /** MENTION */
          tab15.cells[j].innerHTML = uef1234cr1;
        }
      } //tab2 UE SPECIALES


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

        if (j == 2) {
          var ues11cr = listStudent[i][5][6];

          if (listStudent[i][5][0] < 10) {
            ues11cr = 0;
          }

          var ues22cr = listStudent[i][6][6];

          if (listStudent[i][6][0] < 10) {
            ues22cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (listStudent[i][5][0] + listStudent[i][6][0] >= 20) {
            ues12cr1 = listStudent[i][5][6] + listStudent[i][6][6];
          } else {
            ues12cr1 = ues11cr + ues22cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyues1 = listStudent[i][5][3];

          if (moyues1 >= 10 && listStudent[i][5][0] >= 7 && listStudent[i][6][0] >= 7) {} else {
            moyues1 = "--";
          }

          tab23.cells[j].innerHTML = moyues1;
        }

        ;

        if (j == 3) {
          tab23.cells[j].innerHTML = ues12cr1;
        }

        ;
      } //tab3 RESULTATS


      tab3 = temp.children[3];
      tab31 = tab3.children.nested33;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        if (j == 0) {
          tab33.cells[j].innerHTML = listStudent[i][7][1];
        }

        ;

        if (j == 1) {
          moyfs1 = listStudent[i][7][2];

          if (uef1234cr1 + ues12cr1 < 30) {
            moyfs1 = "--";
          }

          tab33.cells[j].innerHTML = moyfs1;
        }

        ;

        if (j == 2) {
          tab33.cells[j].innerHTML = ues12cr1 + uef1234cr1;
        }

        ;

        if (j == 3) {
          tab33.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][7][2]) + 1;
        }

        if (j == 4) {
          tab33.cells[j].innerHTML = ' /';
        }

        ;
      } //Ajoute de la ligne au grand tableau


      worktab.appendChild(temp);
      body.appendChild(page1);
    }
  }

  Page1();

  function PageRattrapage() {
    listStudent = mydata[1];
    rattrapage = mydata[11];
    page2 = document.getElementById('page');
    page2 = page2.cloneNode(true); //Changement Title

    page2.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE RATTRAPAGE 6<sup>eme</sup> SEMESTRE LICENCE PRO L3 MAS EVE 2022-2023";
    bigtab1 = page2.children[0].children[2].children[1]; //Tableau Sur lequel on ajoute les nouvelles lignes

    worktab1 = bigtab1.children[1]; //Ligne des 4 Tableaux

    for (i = 0; i <= mydata[1].length - 1; i++) {
      temp1 = worktab1.children[3].cloneNode(true); //tab0

      tab0r = temp1.children[0];
      tab01r = tab0r.children.nested4;
      tab02r = tab01r.children;
      tab03r = tab02r['0'];
      tab04r = tab03r.children;
      tab05r = tab04r[0]; //good  

      for (j = 0; j <= tab05.childElementCount - 1; j++) {
        if (j == 0) {
          tab05r.cells[j].innerHTML = i + 1;
        }

        if (j == 1) {
          tab05r.cells[j].innerHTML = rattrapage[i][0]['nom'];
        }

        if (j == 2) {
          tab05r.cells[j].innerHTML = rattrapage[i][0]['prenom'];
        }

        if (j == 3) {
          tab05r.cells[j].innerHTML = rattrapage[i][0]['matricule'];
        }
      } //tab1


      tab1 = temp1.children[1];
      tab11 = tab1.children.nested11;
      tab12 = tab11.children;
      tab13 = tab12['0'];
      tab14 = tab13.children;
      tab15 = tab14[0]; //good line

      for (j = 0; j <= tab15.childElementCount - 1; j++) {
        if (j == 0) {
          if (rattrapage[i][1] == 0 || rattrapage[i][1] == null) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = rattrapage[i][1];
          }
        }

        ;

        if (j == 1) {
          if (rattrapage[i][2] == 0 || rattrapage[i][2] == null) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = rattrapage[i][2];
          }
        }

        if (j == 2) {
          if (rattrapage[i][3] == 0 || rattrapage[i][3] == null) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = rattrapage[i][3];
          }
        }

        if (j == 3) {
          if (rattrapage[i][4] == 0 || rattrapage[i][4] == null) {
            tab15.cells[j].innerHTML = '--';
          } else {
            tab15.cells[j].innerHTML = rattrapage[i][4];
          }
        }
        /**MOYENNE GROUPE 1 */


        if (j == 4) {
          var check0 = 0;
          var check1 = 0;
          var check2 = 0;
          var check3 = 0;

          if (listStudent[i][1][0] < 7) {
            check0 = 1;
          }

          if (listStudent[i][2][0] < 7) {
            check1 = 1;
          }

          if (listStudent[i][3][0] < 7) {
            check2 = 1;
          }

          if (listStudent[i][4][0] < 7) {
            check3 = 1;
          }

          check = check0 + check1 + check2 + check3;
          tab15.cells[j].innerHTML = '--'; //if (check > 0) { tab15.cells[j].innerHTML = '--'; } else { tab15.cells[j].innerHTML = listStudent[i][1][3]; }
          //if (listStudent[i][1][3] < 10) { tab15.cells[j].innerHTML = '--'; }

          tab15.cells[j].setAttribute('class', 'titleStyle');
          tab15.cells[j].classList.add('class', 'tdStyle');
        }

        if (j == 5) {
          /*CREDITS*/
          var _creditmat = 0;
          var creditmat4 = 0;

          if (listStudent[i][1][10] == 0) {
            _creditmat = 0;
          } else {
            _creditmat = listStudent[i][1][6];
          }

          tab15.cells[j].setAttribute('class', 'titleStyle');
          tab15.cells[j].classList.add('class', 'tdStyle');
        }
      } //tab2


      tab2 = temp1.children[2];
      tab21 = tab2.children.nested22;
      tab22 = tab21.children['0'];
      tab23 = tab22.children['0'];

      for (j = 0; j <= tab23.childElementCount - 1; j++) {
        if (j == 0) {
          if (rattrapage[i][5] == 0 || rattrapage[i][5] == null) {
            tab23.cells[j].innerHTML = '--';
          } else {
            tab23.cells[j].innerHTML = rattrapage[i][5];
          }
        }

        ;

        if (j == 1) {}
        /*if (listStudent[i][6][11]['note_rattrapage'] == 0 || listStudent[i][6][11]['note_rattrapage'] == null) {
            tab23.cells[j].innerHTML = '--' //listStudent[i][6][0]
        } else {
            tab23.cells[j].innerHTML = listStudent[i][6][11]['note_rattrapage']
        }*/

        /**MOYENNE GROUPE 2 */


        if (j == 2) {
          var check00 = 0;
          var check11 = 0;

          if (listStudent[i][1][0] < 7) {
            check00 = 1;
          }

          if (listStudent[i][2][0] < 7) {
            check11 = 1;
          }

          checka = check00 + check11;
          /*if (checka > 0) { tab23.cells[j].innerHTML = '--'; } else { tab23.cells[j].innerHTML = listStudent[i][5][3]; }
            if (listStudent[i][5][3] < 10) { tab23.cells[j].innerHTML = '--'; }*/

          tab23.cells[j].innerHTML = '--'; //tab23.cells[j].innerHTML = listStudent[i][5][3] 

          tab23.cells[j].setAttribute('class', 'titleStyle');
          tab23.cells[j].classList.add('class', 'tdStyle');
        }

        ;
        /**CREDITS */

        if (j == 3) {
          if (listStudent[i][5][10] == 0 || listStudent[i][5][10] == null) {
            creditmat1 = 0;
          } else {
            creditmat1 = listStudent[i][5][6];
          }
          /*if (listStudent[i][6][11]['note_rattrapage'] == 0 || listStudent[i][6][11]['note_rattrapage'] == null) { creditmat2 = 0 } else { creditmat2 = listStudent[i][6][6] }
            if (listStudent[i][6][11]['note_rattrapage'] == 0 || listStudent[i][6][11]['note_rattrapage'] == null) {
              tab23.cells[j].innerHTML = '--'
          } else {
              tab23.cells[j].innerHTML = creditmat1 + creditmat2
          }*/

          /*if (listStudent[i][5][3] >= 10 && checka <= 0) {
              credit2 = listStudent[i][5][6] + listStudent[i][6][6]
              tab23.cells[j].innerHTML = credit2
          }*/


          tab23.cells[j].setAttribute('class', 'titleStyle');
          tab23.cells[j].classList.add('class', 'tdStyle');
        }

        ;
      } //tab3


      tab3 = temp1.children[3];
      tab31 = tab3.children.nested33;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        if (j == 0) {
          //tab33.cells[j].innerHTML = listStudent[i][7][1] 
          tab33.cells[j].innerHTML = '/';
        }

        ; //Moyenne

        if (j == 1) {
          //if (listStudent[i][7][2] < 10 || (parseInt(tab15.cells[5].innerHTML) + parseInt(tab23.cells[3].innerHTML)) < 30) { tab33.cells[j].innerHTML = '--' } else { tab33.cells[j].innerHTML = listStudent[i][7][2] }
          tab33.cells[j].innerHTML = '/';
        }

        ;

        if (j == 2) {
          //tab33.cells[j] = listStudent[i][1][7] + listStudent[i][2][7] + listStudent[i][3][7] + listStudent[i][4][7] + listStudent[i][5][7] + listStudent[i][6][7]
          tab33.cells[j].innerHTML = '/'; //console.log(parseInt(tab23.cells[3].innerHTML) + 3);
          //tab33.cells[j].innerHTML = parseInt(tab15.cells[5].innerHTML) + parseInt(tab23.cells[3].innerHTML)
        } //listStudent[i][9][3]}; //Nombre de crédits


        if (j == 3) {
          tab33.cells[j].innerHTML = '/';
          /*mydata[2].indexOf(listStudent[i][7][2]) + 1*/
        }

        if (j == 4) {
          tab33.cells[j].innerHTML = ' /';
        }

        ; //listStudent[i][9][3]};
      }

      worktab1.appendChild(temp1);
    } //Ajoute de la ligne au grand tableau


    body.appendChild(page2);
  }

  PageRattrapage();

  function PageSynthese() {
    synthese = mydata[8];
    page2 = document.getElementById('page');
    page2 = page2.cloneNode(true); //Changement Title

    page2.children[0].children[2].children[0].innerHTML = "PROCES VERBAL MODULAIRE SYNTHESE 6<sup>eme</sup> SEMESTRE LICENCE PRO L3 MAS EVE 2022-2023";
    bigtab2 = page2.children[0].children[2].children[1]; //Tableau Sur lequel on ajoute les nouvelles lignes

    worktab2 = bigtab2.children[1];

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
          var uef1cr = synthese[i][1][5];

          if (synthese[i][1][0] < 10) {
            uef1cr = 0;
          }

          var uef2cr = synthese[i][2][5];

          if (synthese[i][2][0] < 10) {
            uef2cr = 0;
          }

          var uef3cr = synthese[i][3][5];

          if (synthese[i][3][0] < 10) {
            uef3cr = 0;
          }

          var uef4cr = synthese[i][4][5];

          if (synthese[i][4][0] < 10) {
            uef4cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (synthese[i][1][0] + synthese[i][2][0] + synthese[i][3][0] + synthese[i][4][0] >= 40) {
            uef1234cr = synthese[i][1][5] + synthese[i][2][5] + synthese[i][3][5] + synthese[i][4][5];
          } else {
            uef1234cr = uef1cr + uef2cr + uef3cr + uef4cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyuef = synthese[i][1][3];

          if (moyuef >= 10 && synthese[i][1][0] >= 7 && synthese[i][2][0] >= 7 && synthese[i][3][0] >= 7 && synthese[i][4][0] >= 7) {//moyuefcr = uef34cr + uef12cr
          } else {
            moyuef = '--';
          }

          tab15.cells[j].innerHTML = moyuef;
        }

        if (j == 5) {
          tab15.cells[j].innerHTML = uef1234cr;
        }
      } //tab2 UE PECIALES


      tab2 = temp2.children[2];
      tab21 = tab2.children.nested22;
      tab22 = tab21.children['0'];
      tab23 = tab22.children['0'];

      for (j = 0; j <= tab23.childElementCount - 1; j++) {
        if (j == 0) {
          tab23.cells[j].innerHTML = synthese[i][5][0];
          /*if (listStudent[i][0]['matricule'] == "EVE22012" || listStudent[i][0]['matricule'] == "EVE22014") {
              tab23.cells[j].innerHTML = '--'
          }*/
        }

        ;

        if (j == 1) {
          tab23.cells[j].innerHTML = synthese[i][6][0];
          /*if (listStudent[i][0]['matricule'] == "EVE22012" || listStudent[i][0]['matricule'] == "EVE22014") {
              tab23.cells[j].innerHTML = '--'
          }*/
        }

        ;

        if (j == 2) {
          var ues1cr = synthese[i][5][5];

          if (synthese[i][5][0] < 10) {
            ues1cr = 0;
          }

          var ues2cr = synthese[i][6][5];

          if (synthese[i][6][0] < 10) {
            ues2cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (synthese[i][5][0] + synthese[i][6][0] >= 20) {
            ues12cr = synthese[i][5][5] + synthese[i][6][5];
          } else {
            ues12cr = ues1cr + ues2cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyues = synthese[i][5][3];

          if (moyues >= 10 && synthese[i][5][0] >= 7 && synthese[i][6][0] >= 7) {} else {
            moyues = "--";
          }

          tab23.cells[j].innerHTML = moyues;
        }

        ;

        if (j == 3) {
          tab23.cells[j].innerHTML = ues12cr;
        }

        ;
      } //tab3 //RESULTATS


      tab3 = temp2.children[3];
      tab31 = tab3.children.nested33;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        if (j == 0) {
          tab33.cells[j].innerHTML = mydata[8][i][7][1];
        }

        ;

        if (j == 1) {
          moyfs = synthese[i][7][2];

          if (uef1234cr + ues12cr < 30) {
            moyfs = "--";
          }

          tab33.cells[j].innerHTML = moyfs;
        }

        ;

        if (j == 2) {
          tab33.cells[j].innerHTML = uef1234cr + ues12cr;
        }

        ;

        if (j == 3) {
          tab33.cells[j].innerHTML = mydata[10].indexOf(synthese[i][7][2]) + 1;
        }

        ;

        if (j == 4) {
          tab33.cells[j].innerHTML = '--';
        }

        ;
      } //Ajoute de la ligne au grand tableau


      worktab2.appendChild(temp2);
      body.appendChild(page2);
    }
  }

  PageSynthese();

  function SyntheseAnnuelle() {
    syntheses5 = mydata[12];
    synthese = mydata[8];
    pageS = document.getElementById('pageS');
    bigtabS = pageS.children[0].children[1].children[1]; //Tableau Sur lequel on ajoute les nouvelles lignes

    worktabS = bigtabS.children[1];

    for (i = 0; i <= mydata[1].length - 1; i++) {
      tempS = worktabS.children[3].cloneNode(true); //tab0 NOMS ET INFOS ETUDIANTS

      tab0 = tempS.children[0];
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
      } //tab1 UEFond S1


      tab1 = tempS.children[1];
      tab11 = tab1.children.nested11;
      tab12 = tab11.children;
      tab13 = tab12['0'];
      tab14 = tab13.children;
      tab15 = tab14[0]; //good line

      for (j = 0; j <= tab15.childElementCount - 1; j++) {
        if (j == 0) {
          tab15.cells[j].innerHTML = syntheses5[i][1][0];
        }

        ;

        if (j == 1) {
          tab15.cells[j].innerHTML = syntheses5[i][2][0];
        }

        if (j == 2) {
          tab15.cells[j].innerHTML = syntheses5[i][3][0];
        }

        if (j == 3) {
          tab15.cells[j].innerHTML = syntheses5[i][4][0];
        }

        if (j == 4) {
          var uef1cr = syntheses5[i][1][5];

          if (syntheses5[i][1][0] < 10) {
            uef1cr = 0;
          }

          var uef2cr = syntheses5[i][2][5];

          if (syntheses5[i][2][0] < 10) {
            uef2cr = 0;
          }

          var uef3cr = syntheses5[i][3][5];

          if (syntheses5[i][3][0] < 10) {
            uef3cr = 0;
          }

          var uef4cr = syntheses5[i][4][5];

          if (syntheses5[i][4][0] < 10) {
            uef4cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (syntheses5[i][1][0] + syntheses5[i][2][0] + syntheses5[i][3][0] + syntheses5[i][4][0] >= 40) {
            uef1234cr = syntheses5[i][1][5] + syntheses5[i][2][5] + syntheses5[i][3][5] + syntheses5[i][4][5];
          } else {
            uef1234cr = uef1cr + uef2cr + uef3cr + uef4cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyuef = syntheses5[i][1][3];

          if (moyuef >= 10 && syntheses5[i][1][0] >= 7 && syntheses5[i][2][0] >= 7 && syntheses5[i][3][0] >= 7 && syntheses5[i][4][0] >= 7) {//moyuefcr = uef34cr + uef12cr
          } else {
            moyuef = '--';
          }

          tab15.cells[j].innerHTML = moyuef;
        }

        if (j == 5) {
          tab15.cells[j].innerHTML = uef1234cr;
        }
      } //tab2 UESP S1


      tab2 = tempS.children[2];
      tab21 = tab2.children.nested22;
      tab22 = tab21.children['0'];
      tab23 = tab22.children['0'];

      for (j = 0; j <= tab23.childElementCount - 1; j++) {
        if (j == 0) {
          tab23.cells[j].innerHTML = syntheses5[i][5][0];
          /*if (listStudent[i][0]['matricule'] == "EVE22012" || listStudent[i][0]['matricule'] == "EVE22014") {
              tab23.cells[j].innerHTML = '--'
          }*/
        }

        ;

        if (j == 1) {
          tab23.cells[j].innerHTML = syntheses5[i][6][0];
          /*if (listStudent[i][0]['matricule'] == "EVE22012" || listStudent[i][0]['matricule'] == "EVE22014") {
              tab23.cells[j].innerHTML = '--'
          }*/
        }

        ;

        if (j == 2) {
          var ues1cr = syntheses5[i][5][5];

          if (syntheses5[i][5][0] < 10) {
            ues1cr = 0;
          }

          var ues2cr = syntheses5[i][6][5];

          if (syntheses5[i][6][0] < 10) {
            ues2cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (syntheses5[i][5][0] + syntheses5[i][6][0] >= 20) {
            ues12cr = syntheses5[i][5][5] + syntheses5[i][6][5];
          } else {
            ues12cr = ues1cr + ues2cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyues = syntheses5[i][5][3];

          if (moyues >= 10 && syntheses5[i][5][0] >= 7 && syntheses5[i][6][0] >= 7) {} else {
            moyues = "--";
          }

          tab23.cells[j].innerHTML = moyues;
        }

        ;

        if (j == 3) {
          tab23.cells[j].innerHTML = ues12cr;
        }

        ;
      } //tab3 UEFond S2


      tab1S = tempS.children[3];
      tab11S = tab1S.children.nested33;
      tab12S = tab11S.children;
      tab13S = tab12S['0'];
      tab14S = tab13S.children;
      tab15S = tab14S[0]; //good line

      for (j = 0; j <= tab15S.childElementCount - 1; j++) {
        if (j == 0) {
          tab15S.cells[j].innerHTML = synthese[i][1][0];
        }

        ;

        if (j == 1) {
          tab15S.cells[j].innerHTML = synthese[i][2][0];
        }

        if (j == 2) {
          tab15S.cells[j].innerHTML = synthese[i][3][0];
        }

        if (j == 3) {
          tab15S.cells[j].innerHTML = synthese[i][4][0];
        }

        if (j == 4) {
          var uef11cr = synthese[i][1][6];

          if (synthese[i][1][0] < 10) {
            uef11cr = 0;
          }

          var uef22cr = listStudent[i][2][6];

          if (listStudent[i][2][0] < 10) {
            uef22cr = 0;
          }

          var uef33cr = listStudent[i][3][6];

          if (synthese[i][3][0] < 10) {
            uef33cr = 0;
          }

          var uef44cr = listStudent[i][4][6];

          if (synthese[i][4][0] < 10) {
            uef44cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (synthese[i][1][0] + synthese[i][2][0] + synthese[i][3][0] + synthese[i][4][0] >= 40) {
            uef1234cr1 = listStudent[i][1][6] + listStudent[i][2][6] + listStudent[i][3][6] + listStudent[i][4][6];
          } else {
            uef1234cr1 = uef11cr + uef22cr + uef33cr + uef44cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyuef1 = synthese[i][1][3];

          if (moyuef1 >= 10 && synthese[i][1][0] >= 7 && synthese[i][2][0] >= 7 && synthese[i][3][0] >= 7 && synthese[i][4][0] >= 7) {//moyuefcr = uef34cr + uef12cr
          } else {
            moyuef1 = '--';
          }

          tab15S.cells[j].innerHTML = moyuef1;
        }

        if (j == 5) {
          /** MENTION */
          tab15S.cells[j].innerHTML = uef1234cr1;
        }
      } //tab4 UESP S2


      tab2S = tempS.children[4];
      tab21S = tab2S.children.nested44;
      tab22S = tab21S.children['0'];
      tab23S = tab22S.children['0'];

      for (j = 0; j <= tab23S.childElementCount - 1; j++) {
        if (j == 0) {
          tab23S.cells[j].innerHTML = synthese[i][5][0];
        }

        ;

        if (j == 1) {
          tab23S.cells[j].innerHTML = synthese[i][6][0];
        }

        if (j == 2) {
          var ues11cr = listStudent[i][5][6];

          if (synthese[i][5][0] < 10) {
            ues11cr = 0;
          }

          var ues22cr = listStudent[i][6][6];

          if (synthese[i][6][0] < 10) {
            ues22cr = 0;
          }
          /**VERIFICATION MODULATION */


          if (synthese[i][5][0] + synthese[i][6][0] >= 20) {
            ues12cr1 = listStudent[i][5][6] + listStudent[i][6][6];
          } else {
            ues12cr1 = ues11cr + ues22cr;
          }
          /**VERIFICATION MOYENNE ET NOTE ELIMINATOIRE */


          moyues1 = synthese[i][5][3];

          if (moyues1 >= 10 && synthese[i][5][0] >= 7 && synthese[i][6][0] >= 7) {} else {
            moyues1 = "--";
          }

          tab23S.cells[j].innerHTML = moyues1;
        }

        ;

        if (j == 3) {
          tab23S.cells[j].innerHTML = ues12cr1;
        }

        ;
      } //tab5 Moy GENE


      tab3 = tempS.children[5];
      tab31 = tab3.children.nested55;
      tab32 = tab31.children['0'];
      tab33 = tab32.children['0'];

      for (j = 0; j <= tab33.childElementCount - 1; j++) {
        if (j == 0) {
          var totCr = sommeInt4(tab15.cells[5].innerHTML, tab23.cells[3].innerHTML, tab15S.cells[5].innerHTML, tab23S.cells[3].innerHTML);

          if (totCr == 60) {
            tab33.cells[j].innerHTML = mydata[13][i];
          } else {
            tab33.cells[j].innerHTML = '--';
          }
        }

        ;

        if (j == 1) {
          /*moyfs = synthese[i][7][2]
          if ((uef1234cr + ues12cr) < 30) {
              moyfs = "--"
          }*/
          tab33.cells[j].innerHTML = sommeInt4(tab15.cells[5].innerHTML, tab23.cells[3].innerHTML, tab15S.cells[5].innerHTML, tab23S.cells[3].innerHTML); //moyfs
        }

        ;
      } //Ajoute de la ligne au grand tableau


      worktabS.appendChild(tempS); //console.log(i);
    }

    body.appendChild(pageS);
  }

  SyntheseAnnuelle();

  function ListeAdmis() {
    moyCredit = mydata[8];
    pageA = document.getElementById('pageA');
    pageA = pageA.cloneNode(true);
    pageA.style.display = "block"; //Changement Title
    //Tbody

    worktabA = pageA.children[0].children[1].children[1].children[1]; //Ligne

    lineA = worktabA.children[0];

    for (i = 0; i <= mydata[1].length - 1; i++) {
      tempA = lineA.cloneNode(true);

      for (j = 0; j <= tempA.childElementCount - 1; j++) {
        if (j == 0) {
          tempA.cells[j].innerHTML = i + 1;
        }

        if (j == 1) {
          tempA.cells[j].innerHTML = moyCredit[i][0]['matricule'];
        }

        if (j == 2) {
          tempA.cells[j].innerHTML = "".concat(moyCredit[i][0]['nom'], "  ").concat(moyCredit[i][0]['prenom']);
        }

        if (j == 3) {
          if (moyCredit[i][0]['sexe'] == "MASCULIN") {
            tempA.cells[j].innerHTML = 'M';
          } else if (moyCredit[i][0]['sexe'] == "FEMININ") {
            tempA.cells[j].innerHTML = 'F';
          }
        }

        if (j == 4) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['moyS1'];

          if (moyCredit[i][7][3]['moyS1'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 5) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['crS1'];

          if (moyCredit[i][7][3]['crS1'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 6) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['moyS2'];

          if (moyCredit[i][7][3]['moyS1'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 7) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['crS2'];

          if (moyCredit[i][7][3]['crS2'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 8) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['moyS3'];

          if (moyCredit[i][7][3]['moyS3'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 9) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['crS3'];

          if (moyCredit[i][7][3]['crS3'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 10) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['moyS4'];

          if (moyCredit[i][7][3]['moyS4'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 11) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['crS4'];

          if (moyCredit[i][7][3]['crS4'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 12) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['moyS5'];

          if (moyCredit[i][7][3]['moyS5'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 13) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['crS5'];

          if (moyCredit[i][7][3]['crS5'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 14) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['moyS6'];

          if (moyCredit[i][7][3]['moyS6'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 15) {
          tempA.cells[j].innerHTML = moyCredit[i][7][3]['crS6'];

          if (moyCredit[i][7][3]['crS6'] == null) {
            tempA.cells[j].innerHTML = '--';
          }
        }

        if (j == 16) {
          tempA.cells[j].innerHTML = sommeMoyFloat6(tempA.cells[4].innerHTML, tempA.cells[6].innerHTML, tempA.cells[8].innerHTML, tempA.cells[10].innerHTML, tempA.cells[12].innerHTML, tempA.cells[14].innerHTML);
        }

        if (j == 17) {
          tempA.cells[j].innerHTML = sommeCrInt6(tempA.cells[5].innerHTML, tempA.cells[7].innerHTML, tempA.cells[9].innerHTML, tempA.cells[11].innerHTML, tempA.cells[13].innerHTML, tempA.cells[15].innerHTML);
        }
      }

      worktabA.appendChild(tempA);
    } //Ajoute de la ligne au grand tableau
    //worktabA.appendChild(temp2)


    lineA.style.display = "none";
    body.appendChild(pageA);
  }

  ListeAdmis();
  /**FUNCTION MULTI_PAGE FOR PROCES VERBAL */

  function ListProcess() {
    body = document.getElementById('body');
    page = document.getElementById('page2');
    listProces = document.createElement('div');

    for (i = 0; i <= 5; i++) {
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
    pagination = clone.children[3]; //Line One
    //Second Line

    line2 = clone.children[1].children[1].children[0];
    line2.children[2].innerHTML = 'MANAGEMENT DES ORGANISATIONS & I.S';
    line2.children[5].innerHTML = '2022/2023'; //Third Line

    line3 = clone.children[1].children[2].children[0];

    if (i == 0) {
      line3.children[1].innerHTML = mydata[9][0]['code_UE']; //"MAS315";

      line3.children[2].innerHTML = mydata[9][0]['intitule_UE']; //"ENVIRONNEMENT INSTITUTIONNEL DE LA PRATIQUE DU SPORT";

      line3.children[4].innerHTML = mydata[5][0];
      line3.children[6].innerHTML = mydata[9][0]['semestre_id']; //'5'

      pagination.innerText = "Page ".concat(i + 1, " / 6");
    }

    if (i == 1) {
      line3.children[1].innerHTML = mydata[9][1]['code_UE']; //"MAS325";

      line3.children[2].innerHTML = mydata[9][1]['intitule_UE']; //"MONTAGE DES PROJETS ET ENTREPRENEURIAT SPORTIF";

      line3.children[4].innerHTML = mydata[5][1];
      line3.children[6].innerHTML = mydata[9][0]['semestre_id'];
      pagination.innerText = "Page ".concat(i + 1, " / 6");
    }

    if (i == 2) {
      line3.children[1].innerHTML = mydata[9][2]['code_UE']; //"MAS335";

      line3.children[2].innerHTML = mydata[9][2]['intitule_UE']; //"INFORMATION ET COMMUNICATION STRATEGIQUES SPORT & L."

      line3.children[4].innerHTML = mydata[5][2];
      line3.children[6].innerHTML = mydata[9][0]['semestre_id'];
      pagination.innerText = "Page ".concat(i + 1, " / 6");
    }

    if (i == 3) {
      line3.children[1].innerHTML = mydata[9][3]['code_UE']; //"MAS345";

      line3.children[2].innerHTML = mydata[9][3]['intitule_UE']; //"E-SPORT"

      line3.children[4].innerHTML = mydata[5][3];
      line3.children[6].innerHTML = mydata[9][0]['semestre_id'];
      pagination.innerText = "Page ".concat(i + 1, " / 6");
    }

    if (i == 4) {
      line3.children[1].innerHTML = mydata[9][4]['code_UE']; //"EVE355";

      line3.children[2].innerHTML = mydata[9][4]['intitule_UE']; //"MULTIMEDIA DANS LE DEVELOPPEMENT DU SPORT & LOISIRS"

      line3.children[4].innerHTML = mydata[5][4];
      line3.children[6].innerHTML = mydata[9][0]['semestre_id'];
      pagination.innerText = "Page ".concat(i + 1, " / 6");
    }

    if (i == 5) {
      line3.children[1].innerHTML = mydata[9][5]['code_UE']; //"EVE365";

      line3.children[2].innerHTML = mydata[9][5]['intitule_UE']; //"INGENIERIE DE L'ANIMATION SPORTIVE ET CULTURELLE"

      line3.children[4].innerHTML = mydata[5][5];
      line3.children[6].innerHTML = mydata[9][0]['semestre_id'];
      pagination.innerText = "Page ".concat(i + 1, " / 6");
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
    } //Tableau des Student


    tab = clone.children[2].children[0];
    listStudent = mydata[1];
    tableContainer = document.getElementById('tableContainer');
    /**STATS */

    for (j = 0; j <= mydata[1].length - 1; j++) {
      line = document.createElement('tr');

      for (k = 0; k <= 9; k++) {
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
          //CC
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][8]);
            /*OK*/
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][8]);
            /*OK*/
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][8]);
            /*OK*/
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][8]);
            /*OK*/
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][8]);
            /*OK*/
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][8]);
            /*OK*/
          }

          td.setAttribute('class', 'cc');
        }

        if (k == 4) {
          //TPE
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][8]);
            /*OK*/
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][8]);
            /*OK*/
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][8]);
            /*OK*/
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][8]);
            /*OK*/
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][8]);
            /*OK*/
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][8]);
            /*OK*/
          }

          td.setAttribute('class', 'cc');
        }

        if (k == 5) {
          //SN
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][9]);
            /*OK*/
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][9]);
            /*OK*/
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][9]);
            /*OK*/
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][9]);
            /*OK*/
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][9]);
            /*OK*/
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][9]);
            /*OK*/
          }
        }

        if (k == 6) {
          //Moyenne
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][0]);
            td.setAttribute('class', 'moyenne');
            /*OK*/
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][0]);
            /*OK*/
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][0]);
            /*OK*/
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][0]);
            /*OK*/
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][0]);
            /*OK*/
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][0]);
            /*OK*/
          }
        }

        if (k == 7) {
          //Crédit
          if (i == 0) {
            td.innerHTML = "".concat(listStudent[j][1][7]);
            /*OK*/
          }

          if (i == 1) {
            td.innerHTML = "".concat(listStudent[j][2][7]);
            /*OK*/
          }

          if (i == 2) {
            td.innerHTML = "".concat(listStudent[j][3][7]);
            /*OK*/
          }

          if (i == 3) {
            td.innerHTML = "".concat(listStudent[j][4][7]);
            /*OK*/
          }

          if (i == 4) {
            td.innerHTML = "".concat(listStudent[j][5][7]);
            /*OK*/
          }

          if (i == 5) {
            td.innerHTML = "".concat(listStudent[j][6][7]);
            /*OK*/
          }
        }

        if (k == 8) {
          //Decision
          if (i == 0) {
            if (listStudent[j][1][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }

            ;
            /*OK*/
          }

          if (i == 1) {
            if (listStudent[j][2][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }

            ;
            /*OK*/
          }

          if (i == 2) {
            if (listStudent[j][3][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }

            ;
            /*OK*/
          }

          if (i == 3) {
            if (listStudent[j][4][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }

            ;
            /*OK*/
          }

          if (i == 4) {
            if (listStudent[j][5][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }

            ;
            /*OK*/
          }

          if (i == 5) {
            if (listStudent[j][6][5]) {
              td.innerHTML = 'Validée';
            } else {
              td.innerHTML = 'Non Validée';
            }

            ;
            /*OK*/
          }
        }

        if (k == 9) {
          //Mention
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

            ;
            /*OK*/
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

            ;
            /*OK*/
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

            ;
            /*OK*/
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

            ;
            /*OK*/
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

            ;
            /*OK*/
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

            ;
            /*OK*/
          }
        }

        line.appendChild(td);
      }

      tab.children[1].appendChild(line);
    }

    return clone;
  }

  ListProcess();
});

function floatfix(a) {
  return (100 - a).toFixed(2);
}

function sommeInt4(a, b, c, d) {
  a = parseInt(a);
  b = parseInt(b);
  c = parseInt(c);
  d = parseInt(d);
  result = a + b + c + d;
  return result;
}

function sommeMoyFloat6(a, b, c, d, e, f) {
  var control = 0;

  if (a == '--') {
    a = 0;
    control += 1;
  }

  if (b == '--') {
    b = 0;
    control += 1;
  }

  if (c == '--') {
    c = 0;
    control += 1;
  }

  if (d == '--') {
    d = 0;
    control += 1;
  }

  if (e == '--') {
    e = 0;
    control += 1;
  }

  if (f == '--') {
    f = 0;
    control += 1;
  }

  a = parseFloat(a);
  b = parseFloat(b);
  c = parseFloat(c);
  d = parseFloat(d);
  e = parseFloat(e);
  f = parseFloat(f);
  result = (a + b + c + d + e + f) / (6 - control);
  result = result.toFixed(2);
  return result;
}

function sommeCrInt6(a, b, c, d, e, f) {
  var control = 0;

  if (a == '--') {
    a = 0;
  }

  if (b == '--') {
    b = 0;
  }

  if (c == '--') {
    c = 0;
  }

  if (d == '--') {
    d = 0;
  }

  if (e == '--') {
    e = 0;
  }

  if (f == '--') {
    f = 0;
  }

  a = parseInt(a);
  b = parseInt(b);
  c = parseInt(c);
  d = parseInt(d);
  e = parseInt(e);
  f = parseInt(f);
  result = a + b + c + d + e + f;
  return result;
}