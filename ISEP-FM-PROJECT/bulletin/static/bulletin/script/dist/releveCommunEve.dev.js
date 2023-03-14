"use strict";

window.addEventListener('load', function () {
  //Recuperation de la variable des données
  mydata = JSON.parse(document.getElementById('semestre1MDS').textContent);
  console.log(mydata);

  function Page1() {
    listStudent = mydata[1];
    bigtab = document.getElementById('table1'); //Tableau Sur lequel on ajoute les nouvelles lignes

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
          tab05.cells[j].innerHTML = i + 1; //tab005.cells[j].innerHTML = i+1;
        }

        if (j == 1) {
          tab05.cells[j].innerHTML = listStudent[i][0]['nom']; //tab005.cells[j].innerHTML = listStudent[i][0]['nom'];
        }

        if (j == 2) {
          tab05.cells[j].innerHTML = listStudent[i][0]['prenom']; //tab005.cells[j].innerHTML = listStudent[i][0]['prenom']
        }

        if (j == 3) {
          tab05.cells[j].innerHTML = listStudent[i][0]['date_naissance']; //tab005.cells[j].innerHTML = listStudent[i][0]['date_naissance']
        }

        if (j == 4) {
          tab05.cells[j].innerHTML = listStudent[i][0]['lieu_naissance']; //tab005.cells[j].innerHTML = listStudent[i][0]['lieu_naissance'];
        }

        if (j == 5) {
          tab05.cells[j].innerHTML = listStudent[i][0]['matricule']; //tab005.cells[j].innerHTML = listStudent[i][0]['matricule'];
        }
      } //tab1


      tab1 = temp.children[1];
      tab11 = tab1.children.nested11;
      tab12 = tab11.children;
      tab13 = tab12['0'];
      tab14 = tab13.children;
      tab15 = tab14[0]; //good line
      //

      /*tab111 = temp1.children[1]
      tab112 = tab111.children.nested11
      tab113 = tab112.children
      tab114 = tab113['0']
      tab115 = tab114.children
      tab116 = tab115['0'] //good line*/

      for (j = 0; j <= tab15.childElementCount - 1; j++) {
        if (j == 0) {
          tab15.cells[j].innerHTML = listStudent[i][1][0]; //tab116.cells[j].innerHTML = listStudent[i][13][1]
        }

        ;

        if (j == 1) {
          //tab116.cells[j].innerHTML = listStudent[i][13][2]
          if (listStudent[i][1][5]) {
            tab15.cells[j].innerHTML = "V";
          } else {
            tab15.cells[j].innerHTML = "NV";
          }
        }

        if (j == 2) {
          tab15.cells[j].innerHTML = listStudent[i][2][0]; //if((listStudent[i][1][0]+listStudent[i][2][0])>=20){tab15.cells[j].innerHTML="V"}else{tab15.cells[j].innerHTML="NV"}
          //tab116.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][13][2])+1;
        }

        if (j == 3) {
          if (listStudent[i][2][5]) {
            tab15.cells[j].innerHTML = "V";
          } else {
            tab15.cells[j].innerHTML = "NV";
          } //tab15.cells[j].innerHTML=listStudent[i][3][0]

        }

        if (j == 4) {
          tab15.cells[j].innerHTML = listStudent[i][3][0]; //tab116.cells[j].innerHTML= '/'
        }

        if (j == 5) {
          if (listStudent[i][3][5]) {
            tab15.cells[j].innerHTML = "V";
          } else {
            tab15.cells[j].innerHTML = "NV";
          } //tab116.cells[j].innerHTML= '/'

        }

        if (j == 6) {
          tab15.cells[j].innerHTML = listStudent[i][4][0]; //tab116.cells[j].innerHTML= '/'
        }

        if (j == 7) {
          if (listStudent[i][4][5]) {
            tab15.cells[j].innerHTML = "V";
          } else {
            tab15.cells[j].innerHTML = "NV";
          } //tab116.cells[j].innerHTML= '/'

        }

        if (j == 8) {
          tab15.cells[j].innerHTML = listStudent[i][1][3]; //tab116.cells[j].innerHTML= '/'
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
          if (listStudent[i][5][5]) {
            tab23.cells[j].innerHTML = 'V';
          } else {
            tab23.cells[j].innerHTML = 'NV';
          }
        }

        ;

        if (j == 2) {
          tab23.cells[j].innerHTML = listStudent[i][6][0];
        }

        ;

        if (j == 3) {
          if (listStudent[i][6][5]) {
            tab23.cells[j].innerHTML = 'V';
          } else {
            tab23.cells[j].innerHTML = 'NV';
          }
        }

        ;

        if (j == 4) {
          tab23.cells[j].innerHTML = listStudent[i][5][3];
        }

        ;
      } //tab3


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
          tab33.cells[j].innerHTML = listStudent[i][7][2];
        }

        ;

        if (j == 2) {
          tab33.cells[j].innerHTML = mydata[2].indexOf(listStudent[i][7][2]) + 1;
        }

        if (j == 3) {
          tab33.cells[j].innerHTML = listStudent[i][1][7] + listStudent[i][2][7] + listStudent[i][3][7] + listStudent[i][4][7] + listStudent[i][5][7] + listStudent[i][6][7];
        } //listStudent[i][9][3]}; //Nombre de crédits


        if (j == 4) {
          tab33.cells[j].innerHTML = ' /';
        }

        ; //listStudent[i][9][3]};
      } //Ajoute de la ligne au grand tableau


      worktab.appendChild(temp);
    }
  } //Page1()

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
    //Line One
    //Second Line
    line2 = clone.children[1].children[1].children[0];
    line2.children[2].innerHTML = 'MANAGEMENT DES ORGANISATIONS & I.S';
    line2.children[5].innerHTML = '2022/2023'; //Third Line

    line3 = clone.children[1].children[2].children[0];

    if (i == 0) {
      line3.children[1].innerHTML = "MAS315";
      line3.children[2].innerHTML = "ENVIRONNEMENT INSTITUTIONNEL DE LA PRATIQUE DU SPORT";
      line3.children[4].innerHTML = mydata[5][0];
      line3.children[5].innerHTML = '5';
    }

    if (i == 1) {
      line3.children[1].innerHTML = "MAS325";
      line3.children[2].innerHTML = "MONTAGE DES PEOJETS ET ENTREPRENEURIAT SPORTIF";
      line3.children[4].innerHTML = mydata[5][1];
      line3.children[5].innerHTML = '5';
    }

    if (i == 2) {
      line3.children[1].innerHTML = "MAS335";
      line3.children[2].innerHTML = "INFORMATION ET COMMUNICATION STRATEGIQUES SPORT & L.";
      line3.children[4].innerHTML = mydata[5][2];
      line3.children[5].innerHTML = '5';
    }

    if (i == 3) {
      line3.children[1].innerHTML = "MAS345";
      line3.children[2].innerHTML = "E-SPORT";
      line3.children[4].innerHTML = mydata[5][3];
      line3.children[5].innerHTML = '5';
    }

    if (i == 4) {
      line3.children[1].innerHTML = "EVE355";
      line3.children[2].innerHTML = "MULTIMEDIA DANS LE DEVELOPPEMENT DU SPORT & LOISIRS";
      line3.children[4].innerHTML = mydata[5][4];
      line3.children[5].innerHTML = '5';
    }

    if (i == 5) {
      line3.children[1].innerHTML = "EVE365";
      line3.children[2].innerHTML = "INGENIERIE DE L'ANIMATION SPORTIVE ET CULTURELLE";
      line3.children[4].innerHTML = mydata[5][5];
      line3.children[5].innerHTML = '5';
    } //Tableau des Student


    tab = clone.children[2].children[0];

    for (j = 0; j <= mydata[1].length - 1; j++) {
      line = document.createElement('tr');

      for (k = 0; k <= 8; k++) {
        td = document.createElement('td');

        if (k == 0) {
          td.innerHTML = "".concat(j + 1);
        }

        if (k == 1) {}

        if (k == 2) {}

        if (k == 3) {}

        if (k == 4) {}

        if (k == 5) {}

        if (k == 6) {}

        if (k == 7) {}

        if (k == 8) {}

        line.appendChild(td);
      }

      tab.children[1].appendChild(line);
    }

    return clone;
  }

  ListProcess();
});