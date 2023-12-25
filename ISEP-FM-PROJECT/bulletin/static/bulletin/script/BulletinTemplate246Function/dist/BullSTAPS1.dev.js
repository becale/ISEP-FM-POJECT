"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.BullSTAPS1 = BullSTAPS1;

function BullSTAPS1(clone, i, mydata) {
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
      if (listStudent[i][1][0] >= 7 && listStudent[i][1][0] < 10 && listStudent[i][1][3] >= 10) {
        ligneEPS111.children[j].innerHTML = "Validée";
      } else if (listStudent[i][1][0] >= 10) {
        ligneEPS111.children[j].innerHTML = "Validée";
      } else if (listStudent[i][1][0] < 10) {
        ligneEPS111.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 10) {
      ligneEPS111.children[j].innerHTML = mydata[4];
    } //Session


    if (j == 11) {
      if (listStudent[i][1][0] >= 7 && listStudent[i][1][2] >= 10 || listStudent[i][1][0] >= 10) {
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
      //if (listStudent[i][2][5]) { ligneEPS112.children[6].innerHTML = "Validée" } else { ligneEPS112.children[6].innerHTML = "Non validée" }
      if (listStudent[i][2][0] >= 7 && listStudent[i][2][0] < 10 && listStudent[i][1][3] >= 10) {
        ligneEPS112.children[j].innerHTML = "Validée";
      } else if (listStudent[i][2][0] >= 10) {
        ligneEPS112.children[j].innerHTML = "Validée";
      } else if (listStudent[i][2][0] < 10) {
        ligneEPS112.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      ligneEPS112.children[j].innerHTML = mydata[4];
    } //Session


    if (j == 8) {
      //if (listStudent[i][2][5]) { ligneEPS112.children[j].innerHTML = listStudent[i][2][6] } else { ligneEPS112.children[j].innerHTML = 0 } 
      if (listStudent[i][2][0] >= 7 && listStudent[i][1][2] >= 10 || listStudent[i][2][0] >= 10) {
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
      if (listStudent[i][3][0] >= 7 && listStudent[i][3][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS113.children[j].innerHTML = "Validée";
      } else if (listStudent[i][2][0] >= 10) {
        ligneEPS113.children[j].innerHTML = "Validée";
      } else if (listStudent[i][3][0] < 10) {
        ligneEPS113.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 9) {
      ligneEPS113.children[j].innerHTML = mydata[4];
    } // Session


    if (j == 10) {
      if (listStudent[i][3][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][3][0] >= 10) {
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
      if (listStudent[i][4][0] >= 7 && listStudent[i][4][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS114.children[j].innerHTML = "Validée";
      } else if (listStudent[i][4][0] >= 10) {
        ligneEPS114.children[j].innerHTML = "Validée";
      } else if (listStudent[i][4][0] < 10) {
        ligneEPS114.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 7) {
      ligneEPS114.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][4][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][4][0] >= 10) {
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
      if (listStudent[i][5][0] >= 7 && listStudent[i][5][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS115a.children[j].innerHTML = "Validée";
      } else if (listStudent[i][5][0] >= 10) {
        ligneEPS115a.children[j].innerHTML = "Validée";
      } else if (listStudent[i][5][0] < 10) {
        ligneEPS115a.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 7) {
      ligneEPS115a.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][5][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][5][0] >= 10) {
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
      if (listStudent[i][6][0] >= 7 && listStudent[i][6][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS115b.children[j].innerHTML = "Validée";
      } else if (listStudent[i][6][0] >= 10) {
        ligneEPS115b.children[j].innerHTML = "Validée";
      } else if (listStudent[i][6][0] < 10) {
        ligneEPS115b.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 7) {
      ligneEPS115b.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][6][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][6][0] >= 10) {
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
      if (listStudent[i][7][0] >= 7 && listStudent[i][7][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS115j.children[j].innerHTML = "Validée";
      } else if (listStudent[i][7][0] >= 10) {
        ligneEPS115j.children[j].innerHTML = "Validée";
      } else if (listStudent[i][7][0] < 10) {
        ligneEPS115j.children[j].innerHTML = "Non validée";
      } //if (listStudent[i][7][5]) { ligneEPS115j.children[j].innerHTML = "Validée" } else { ligneEPS115j.children[j].innerHTML = "Non validée" } 

    } //Mention


    if (j == 7) {
      ligneEPS115j.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][7][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][7][0] >= 10) {
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
      if (listStudent[i][8][0] >= 7 && listStudent[i][8][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS115l.children[j].innerHTML = "Validée";
      } else if (listStudent[i][8][0] >= 10) {
        ligneEPS115l.children[j].innerHTML = "Validée";
      } else if (listStudent[i][8][0] < 10) {
        ligneEPS115l.children[j].innerHTML = "Non validée";
      } //if (listStudent[i][8][5]) { ligneEPS115l.children[j].innerHTML = "Validée" } else { ligneEPS115l.children[j].innerHTML = "Non validée" } 

    } //Mention


    if (j == 7) {
      ligneEPS115l.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][8][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][8][0] >= 10) {
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
      if (listStudent[i][8][0] >= 7 && listStudent[i][9][0] < 10 && listStudent[i][3][3] >= 10) {
        ligneEPS116.children[j].innerHTML = "Validée";
      } else if (listStudent[i][9][0] >= 10) {
        ligneEPS116.children[j].innerHTML = "Validée";
      } else if (listStudent[i][9][0] < 10) {
        ligneEPS116.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 7) {
      ligneEPS116.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][9][0] >= 7 && listStudent[i][3][3] >= 10 || listStudent[i][9][0] >= 10) {
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
      if (listStudent[i][10][0] >= 7 && listStudent[i][10][0] < 10 && listStudent[i][10][3] >= 10) {
        ligneEPS117.children[j].innerHTML = "Validée";
      } else if (listStudent[i][10][0] >= 10) {
        ligneEPS117.children[j].innerHTML = "Validée";
      } else if (listStudent[i][10][0] < 10) {
        ligneEPS117.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 9) {
      ligneEPS117.children[j].innerHTML = mydata[4];
    } // Session


    if (j == 10) {
      if (listStudent[i][10][0] >= 7 && listStudent[i][10][3] >= 10 || listStudent[i][10][0] >= 10 || listStudent[i][10][0] >= 10) {
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
      if (listStudent[i][11][0] >= 7 && listStudent[i][11][0] < 10 && listStudent[i][10][3] >= 10) {
        ligneEPS118.children[j].innerHTML = "Validée";
      } else if (listStudent[i][11][0] >= 10) {
        ligneEPS118.children[j].innerHTML = "Validée";
      } else if (listStudent[i][11][0] < 10) {
        ligneEPS118.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 7) {
      ligneEPS118.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][11][0] >= 7 && listStudent[i][10][3] >= 10 || listStudent[i][11][0] >= 10) {
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
      //if (listStudent[i][12][5]) { ligneEPS119.children[j].innerHTML = "Validée" } else { ligneEPS119.children[j].innerHTML = "Non validée" } 
      if (listStudent[i][12][0] >= 7 && listStudent[i][12][0] < 10 && listStudent[i][10][3] >= 10) {
        ligneEPS119.children[j].innerHTML = "Validée";
      } else if (listStudent[i][12][0] >= 10) {
        ligneEPS119.children[j].innerHTML = "Validée";
      } else if (listStudent[i][12][0] < 10) {
        ligneEPS119.children[j].innerHTML = "Non validée";
      }
    } //Mention


    if (j == 7) {
      ligneEPS119.children[j].innerHTML = mydata[4];
    } //session


    if (j == 8) {
      if (listStudent[i][12][0] >= 7 && listStudent[i][10][3] >= 10 || listStudent[i][12][0] >= 10) {
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
  /*********************************************************************SEMESTRE 2 STAPS ************************************************************* */


  data2 = mydata[6];
  s2eps = clone.childNodes[2].children[3];
  s2epsbody = s2eps.children[0].children[1]; //Ligne 1

  ligne11 = s2epsbody.children[0];
  ligne11.children[0].innerHTML = "SEMESTRE 2";
  ligne11.children[2].innerHTML = "EPS121";
  ligne11.children[3].innerHTML = "Activités phyiques adaptées - Sport pour tous";

  for (j = 0; j <= ligne11.childElementCount - 1; j++) {
    if (j == 4) {
      ligne11.children[j].innerHTML = data2[i][1][0];
    }

    if (j == 5) {
      ligne11.children[j].innerHTML = data2[i][1][1];
    }

    if (j == 6) {
      ligne11.children[j].innerHTML = data2[i][1][2];
    }

    if (j == 7) {
      ligne11.children[j].innerHTML = data2[i][1][3];
    }

    if (j == 8) {
      ligne11.children[j].innerHTML = data2[i][1][4];
    }

    if (j == 9) {
      //if (data2[i][1][5]) { ligne11.children[j].innerHTML = "Validée" } else { ligne11.children[j].innerHTML = "Non validée" }
      if (data2[i][1][0] >= 7 && data2[i][1][0] < 10 && data2[i][1][3] >= 10) {
        ligne11.children[j].innerHTML = "Validée";
      } else if (data2[i][1][0] >= 10) {
        ligne11.children[j].innerHTML = "Validée";
      } else if (data2[i][1][0] < 10) {
        ligne11.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 10) {
      if (data2[i][1][8]) {
        ligne11.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne11.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 11) {
      if (data2[i][1][0] >= 7 && data2[i][1][3] >= 10 || data2[i][1][0] >= 10) {
        ligne11.children[j].innerHTML = data2[i][1][6];
      } else {
        ligne11.children[j].innerHTML = 0;
      }
    }
  } //Ligne 2


  ligne22 = s2epsbody.children[1];
  ligne22.children[0].innerHTML = "EPS122";
  ligne22.children[1].innerHTML = "Traumatologie - Premiers secours";

  for (j = 0; j <= ligne22.childElementCount - 1; j++) {
    if (j == 2) {
      ligne22.children[j].innerHTML = data2[i][2][0];
    }

    if (j == 3) {
      ligne22.children[j].innerHTML = data2[i][2][1];
    }

    if (j == 4) {
      ligne22.children[j].innerHTML = data2[i][2][2];
    }

    if (j == 5) {
      ligne22.children[j].innerHTML = data2[i][2][4];
    }

    if (j == 6) {
      if (data2[i][2][0] >= 7 && data2[i][2][0] < 10 && data2[i][1][3] >= 10) {
        ligne22.children[j].innerHTML = "Validée";
      } else if (data2[i][2][0] >= 10) {
        ligne22.children[j].innerHTML = "Validée";
      } else if (data2[i][2][0] < 10) {
        ligne22.children[j].innerHTML = "Non validée";
      } //if (data2[i][2][5]) { ligne22.children[j].innerHTML = "Validée" } else { ligne22.children[j].innerHTML = "Non validée" } 

    }

    if (j == 7) {
      if (data2[i][2][8]) {
        ligne22.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne22.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][2][0] >= 7 && data2[i][1][3] >= 10 || data2[i][2][0] >= 10) {
        ligne22.children[j].innerHTML = data2[i][2][6];
      } else {
        ligne22.children[j].innerHTML = 0;
      } //ligne22.children[j].innerHTML = data2[i][2][7] 

    }
  } //Ligne 3


  ligne33 = s2epsbody.children[2]; //ligne33.children[0].innerHTML = "SEMESTRE 2"

  ligne33.children[1].innerHTML = "EPS123";
  ligne33.children[2].innerHTML = "Théorie et Méthodologie de l'entrainement";

  for (j = 0; j <= ligne33.childElementCount - 1; j++) {
    if (j == 3) {
      ligne33.children[j].innerHTML = data2[i][3][0];
    }

    if (j == 4) {
      ligne33.children[j].innerHTML = data2[i][3][1];
    }

    if (j == 5) {
      ligne33.children[j].innerHTML = data2[i][3][2];
    }

    if (j == 6) {
      ligne33.children[j].innerHTML = data2[i][3][3];
    }

    if (j == 7) {
      ligne33.children[j].innerHTML = data2[i][3][4];
    }

    if (j == 8) {
      if (data2[i][3][0] >= 7 && data2[i][3][0] < 10 && data2[i][3][3] >= 10) {
        ligne33.children[j].innerHTML = "Validée";
      } else if (data2[i][3][0] >= 10) {
        ligne33.children[j].innerHTML = "Validée";
      } else if (data2[i][2][0] < 10) {
        ligne33.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 9) {
      if (data2[i][3][8]) {
        ligne33.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne33.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 10) {
      if (data2[i][3][0] >= 7 && data2[i][3][3] >= 10 || data2[i][2][0] >= 10) {
        ligne33.children[j].innerHTML = data2[i][3][6];
      } else {
        ligne33.children[j].innerHTML = 0;
      } //ligne33.children[j].innerHTML = data2[i][3][7] 

    } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 

  } //Ligne 4


  ligne44 = s2epsbody.children[3]; //ligne44.children[0].innerHTML = "SEMESTRE 2"

  ligne44.children[0].innerHTML = "EPS124";
  ligne44.children[1].innerHTML = "Anatomie II";

  for (j = 0; j <= ligne44.childElementCount - 1; j++) {
    if (j == 2) {
      ligne44.children[j].innerHTML = data2[i][4][0];
    }

    if (j == 3) {
      ligne44.children[j].innerHTML = data2[i][4][1];
    }

    if (j == 4) {
      ligne44.children[j].innerHTML = data2[i][4][2];
    }

    if (j == 5) {
      ligne44.children[j].innerHTML = data2[i][4][4];
    }

    if (j == 6) {
      if (data2[i][4][0] >= 7 && data2[i][4][0] < 10 && data2[i][3][3] >= 10) {
        ligne44.children[j].innerHTML = "Validée";
      } else if (data2[i][4][0] >= 10) {
        ligne44.children[j].innerHTML = "Validée";
      } else if (data2[i][4][0] < 10) {
        ligne44.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][4][8]) {
        ligne44.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne44.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][4][0] >= 7 && data2[i][3][3] >= 10 || data2[i][4][0] >= 10) {
        ligne44.children[j].innerHTML = data2[i][4][6];
      } else {
        ligne44.children[j].innerHTML = 0;
      }
    }
  } //Ligne 5


  ligne55 = s2epsbody.children[4]; //ligne55.children[0].innerHTML = "SEMESTRE 2"

  ligne55.children[0].innerHTML = "EPS125";
  ligne55.children[1].innerHTML = "Didactique de APS: Athlétisme II";

  for (j = 0; j <= ligne55.childElementCount - 1; j++) {
    if (j == 2) {
      ligne55.children[j].innerHTML = data2[i][5][0];
    }

    if (j == 3) {
      ligne55.children[j].innerHTML = data2[i][5][1];
    }

    if (j == 4) {
      ligne55.children[j].innerHTML = data2[i][5][2];
    }

    if (j == 5) {
      ligne55.children[j].innerHTML = data2[i][4][4];
    }

    if (j == 6) {
      if (data2[i][5][0] >= 7 && data2[i][5][0] < 10 && data2[i][3][3] >= 10) {
        ligne55.children[j].innerHTML = "Validée";
      } else if (data2[i][5][0] >= 10) {
        ligne55.children[j].innerHTML = "Validée";
      } else if (data2[i][5][0] < 10) {
        ligne55.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][5][8]) {
        ligne55.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne55.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][5][0] >= 7 && data2[i][3][3] >= 10 || data2[i][5][0] >= 10) {
        ligne55.children[j].innerHTML = data2[i][5][6];
      } else {
        ligne55.children[j].innerHTML = 0;
      } //ligne55.children[j].innerHTML = data2[i][5][7] 

    }
  } //Ligne 6


  ligne66 = s2epsbody.children[5]; //ligne66.children[0].innerHTML = "SEMESTRE 2"

  ligne66.children[0].innerHTML = "EPS125";
  ligne66.children[1].innerHTML = "Didactique de APS: Gymnastique";

  for (j = 0; j <= ligne66.childElementCount - 1; j++) {
    if (j == 2) {
      ligne66.children[j].innerHTML = data2[i][6][0];
    }

    if (j == 3) {
      ligne66.children[j].innerHTML = data2[i][6][1];
    }

    if (j == 4) {
      ligne66.children[j].innerHTML = data2[i][6][2];
    } //if (j == 5) { ligne66.children[j].innerHTML = data2[i][4][3] }


    if (j == 5) {
      ligne66.children[j].innerHTML = data2[i][6][4];
    }

    if (j == 6) {
      if (data2[i][6][0] >= 7 && data2[i][6][0] < 10 && data2[i][3][3] >= 10) {
        ligne66.children[j].innerHTML = "Validée";
      } else if (data2[i][6][0] >= 10) {
        ligne66.children[j].innerHTML = "Validée";
      } else if (data2[i][6][0] < 10) {
        ligne66.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][6][8]) {
        ligne66.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne66.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][6][0] >= 7 && data2[i][3][3] >= 10 || data2[i][6][0] >= 10) {
        ligne66.children[j].innerHTML = data2[i][6][6];
      } else {
        ligne66.children[j].innerHTML = 0;
      }
    }
  } //Ligne 7


  ligne77 = s2epsbody.children[6]; //ligne77.children[0].innerHTML = "SEMESTRE 2"

  ligne77.children[0].innerHTML = "EPS125";
  ligne77.children[1].innerHTML = "Didactique de APS: Judo";

  for (j = 0; j <= ligne77.childElementCount - 1; j++) {
    if (j == 2) {
      ligne77.children[j].innerHTML = data2[i][7][0];
    }

    if (j == 3) {
      ligne77.children[j].innerHTML = data2[i][7][1];
    }

    if (j == 4) {
      ligne77.children[j].innerHTML = data2[i][7][2];
    } //if (j == 5) { ligne77.children[j].innerHTML = data2[i][4][3] }


    if (j == 5) {
      ligne77.children[j].innerHTML = data2[i][7][4];
    }

    if (j == 6) {
      if (data2[i][7][0] >= 7 && data2[i][7][0] < 10 && data2[i][3][3] >= 10) {
        ligne77.children[j].innerHTML = "Validée";
      } else if (data2[i][7][0] >= 10) {
        ligne77.children[j].innerHTML = "Validée";
      } else if (data2[i][7][0] < 10) {
        ligne77.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][7][8]) {
        ligne77.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne77.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][7][0] >= 7 && data2[i][3][3] >= 10 || data2[i][7][0] >= 10) {
        ligne77.children[j].innerHTML = data2[i][7][6];
      } else {
        ligne77.children[j].innerHTML = 0;
      }
    }
  } //Ligne 8


  ligne88 = s2epsbody.children[7]; //ligne88.children[0].innerHTML = "SEMESTRE 2"

  ligne88.children[0].innerHTML = "EPS125";
  ligne88.children[1].innerHTML = "Didactique de APS: Football";

  for (j = 0; j <= ligne88.childElementCount - 1; j++) {
    if (j == 2) {
      ligne88.children[j].innerHTML = data2[i][8][0];
    }

    if (j == 3) {
      ligne88.children[j].innerHTML = data2[i][8][1];
    }

    if (j == 4) {
      ligne88.children[j].innerHTML = data2[i][8][2];
    } //if (j == 5) { ligne88.children[j].innerHTML = data2[i][4][3] }


    if (j == 5) {
      ligne88.children[j].innerHTML = data2[i][8][4];
    }

    if (j == 6) {
      if (data2[i][8][0] >= 7 && data2[i][8][0] < 10 && data2[i][3][3] >= 10) {
        ligne88.children[j].innerHTML = "Validée";
      } else if (data2[i][8][0] >= 10) {
        ligne88.children[j].innerHTML = "Validée";
      } else if (data2[i][8][0] < 10) {
        ligne88.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][8][8]) {
        ligne88.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne88.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][8][0] >= 7 && data2[i][3][3] >= 10 || data2[i][8][0] >= 10) {
        ligne88.children[j].innerHTML = data2[i][8][6];
      } else {
        ligne88.children[j].innerHTML = 0;
      }
    }
  } //Ligne 9


  ligne99 = s2epsbody.children[8]; //ligne99.children[0].innerHTML = "SEMESTRE 2"

  ligne99.children[0].innerHTML = "EPS126";
  ligne99.children[1].innerHTML = "Pédagogie pratique";

  for (j = 0; j <= ligne99.childElementCount - 1; j++) {
    if (j == 2) {
      ligne99.children[j].innerHTML = data2[i][9][0];
    }

    if (j == 3) {
      ligne99.children[j].innerHTML = data2[i][9][1];
    }

    if (j == 4) {
      ligne99.children[j].innerHTML = data2[i][9][2];
    } //if (j == 5) { ligne99.children[j].innerHTML = data2[i][4][3] }


    if (j == 5) {
      ligne99.children[j].innerHTML = data2[i][9][4];
    }

    if (j == 6) {
      if (data2[i][9][0] >= 7 && data2[i][9][0] < 10 && data2[i][3][3] >= 10) {
        ligne99.children[j].innerHTML = "Validée";
      } else if (data2[i][9][0] >= 10) {
        ligne99.children[j].innerHTML = "Validée";
      } else if (data2[i][9][0] < 10) {
        ligne99.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][9][8]) {
        ligne99.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne99.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][9][0] >= 7 && data2[i][3][3] >= 10 || data2[i][9][0] >= 10) {
        ligne99.children[j].innerHTML = data2[i][9][6];
      } else {
        ligne99.children[j].innerHTML = 0;
      }
    }
  } //Ligne 10


  ligne100 = s2epsbody.children[9]; //ligne100.children[0].innerHTML = "SEMESTRE 2"

  ligne100.children[1].innerHTML = "EPS127";
  ligne100.children[2].innerHTML = "Technique d'expression française II";

  for (j = 0; j <= ligne100.childElementCount - 1; j++) {
    if (j == 3) {
      ligne100.children[j].innerHTML = data2[i][10][0];
    }

    if (j == 4) {
      ligne100.children[j].innerHTML = data2[i][10][1];
    }

    if (j == 5) {
      ligne100.children[j].innerHTML = data2[i][10][2];
    }

    if (j == 6) {
      ligne100.children[j].innerHTML = data2[i][10][3];
    }

    if (j == 7) {
      ligne100.children[j].innerHTML = data2[i][10][4];
    }

    if (j == 8) {
      if (data2[i][10][0] >= 7 && data2[i][10][0] < 10 && data2[i][10][3] >= 10) {
        ligne100.children[j].innerHTML = "Validée";
      } else if (data2[i][10][0] >= 10) {
        ligne100.children[j].innerHTML = "Validée";
      } else if (data2[i][10][0] < 10) {
        ligne100.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 9) {
      if (data2[i][10][8]) {
        ligne100.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne100.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 10) {
      if (data2[i][10][0] >= 7 && data2[i][10][3] >= 10 || data2[i][10][0] >= 10) {
        ligne100.children[j].innerHTML = data2[i][10][6];
      } else {
        ligne100.children[j].innerHTML = 0;
      }
    } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 

  } //Ligne 11


  ligne111 = s2epsbody.children[10]; //ligne111.children[0].innerHTML = "SEMESTRE 2"

  ligne111.children[0].innerHTML = "EPS128";
  ligne111.children[1].innerHTML = "Droit du sport";

  for (j = 0; j <= ligne111.childElementCount - 1; j++) {
    if (j == 2) {
      ligne111.children[j].innerHTML = data2[i][11][0];
    }

    if (j == 3) {
      ligne111.children[j].innerHTML = data2[i][11][1];
    }

    if (j == 4) {
      ligne111.children[j].innerHTML = data2[i][11][2];
    } //if (j == 6) { ligne111.children[j].innerHTML = data2[i][11][3] }


    if (j == 5) {
      ligne111.children[j].innerHTML = data2[i][11][4];
    }

    if (j == 6) {
      if (data2[i][11][0] >= 7 && data2[i][11][0] < 10 && data2[i][10][3] >= 10) {
        ligne111.children[j].innerHTML = "Validée";
      } else if (data2[i][11][0] >= 10) {
        ligne111.children[j].innerHTML = "Validée";
      } else if (data2[i][11][0] < 10) {
        ligne111.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][11][8]) {
        ligne111.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne111.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][11][0] >= 7 && data2[i][10][3] >= 10 || data2[i][11][0] >= 10) {
        ligne111.children[j].innerHTML = data2[i][11][6];
      } else {
        ligne111.children[j].innerHTML = 0;
      }
    } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 

  } //Ligne 12


  ligne112 = s2epsbody.children[11]; //ligne111.children[0].innerHTML = "SEMESTRE 2"

  ligne112.children[0].innerHTML = "EPS129";
  ligne112.children[1].innerHTML = "Stage-Pratique";

  for (j = 0; j <= ligne112.childElementCount - 1; j++) {
    if (j == 2) {
      ligne112.children[j].innerHTML = data2[i][12][0];
    }

    if (j == 3) {
      ligne112.children[j].innerHTML = data2[i][12][1];
    }

    if (j == 4) {
      ligne112.children[j].innerHTML = data2[i][12][2];
    } //if (j == 6) { ligne112.children[j].innerHTML = data2[i][11][3] }


    if (j == 5) {
      ligne112.children[j].innerHTML = data2[i][12][4];
    }

    if (j == 6) {
      if (data2[i][2][0] >= 7 && data2[i][12][0] < 10 && data2[i][10][3] >= 10) {
        ligne112.children[j].innerHTML = "Validée";
      } else if (data2[i][12][0] >= 10) {
        ligne112.children[j].innerHTML = "Validée";
      } else if (data2[i][12][0] < 10) {
        ligne112.children[j].innerHTML = "Non validée";
      }
    }

    if (j == 7) {
      if (data2[i][12][8]) {
        ligne112.children[j].innerHTML = 'Rattrapage';
      } else {
        ligne112.children[j].innerHTML = mydata[9];
      }
    }

    if (j == 8) {
      if (data2[i][12][0] >= 7 && data2[i][10][3] >= 10 || data2[i][12][0] >= 10) {
        ligne112.children[j].innerHTML = data2[i][11][6];
      } else {
        ligne112.children[j].innerHTML = 0;
      }
    } //else { ligne11.children[j].innerHTML = 0,  + data2[i][2][0]) >= 20 

  } //Ligne 13

  /*var ligne13 = document.getElementById('ligne-13')
  ligne13.style.backgroundColor = "#C7B54D"*/
  //LIGNE 11


  s2epsResult = s2epsbody.children[12];
  s2epsResult.style.backgroundColor = "#C7B54D";
  s2epsResult.children[0].innerHTML = "RESULTATS SEMESTRE 2";
  s2epsResult.children[5].innerHTML = "Total Crédits Semestre 2";

  for (j = 0; j <= s2epsResult.childElementCount - 1; j++) {
    if (j == 1) {
      s2epsResult.children[j].innerHTML = data2[i][13][0];
    }

    if (j == 2) {
      s2epsResult.children[j].innerHTML = data2[i][13][1];
    }

    if (j == 3) {
      s2epsResult.children[j].innerHTML = data2[i][13][2];
    }

    if (j == 4) {
      s2epsResult.children[j].innerHTML = mydata[7].indexOf(data2[i][13][2]) + 1;
    }

    if (j == 6) {
      s2epsResult.children[j].innerHTML = sommeInt9(ligne11.children[11].innerHTML, ligne22.children[8].innerHTML, ligne33.children[10].innerHTML, ligne44.children[8].innerHTML, ligne55.children[8].innerHTML, ligne99.children[8].innerHTML, ligne100.children[10].innerHTML, ligne111.children[8].innerHTML, ligne112.children[8].innerHTML);
    } //(data2[i][1][7] + data2[i][2][7] + data2[i][3][7] + data2[i][4][7] + data2[i][5][7] + data2[i][9][7] + data2[i][10][7] + data2[i][11][7] + data2[i][12][7]) }

  }
  /**RESULTATS S1 & S2 MDS */


  s1s2epsrecap = clone.children[2].children[4].children[1].children[1];

  for (j = 0; j <= s1s2epsrecap.childElementCount - 1; j++) {
    if (j == 0) {
      s1s2epsrecap.children[j].innerHTML = sommeInt2(resultat.children[1].innerHTML, s2epsResult.children[1].innerHTML);
    }

    if (j == 1) {
      s1s2epsrecap.children[j].innerHTML = sommeFloat2(resultat.children[2].innerHTML, s2epsResult.children[2].innerHTML);
    }

    if (j == 2) {
      s1s2epsrecap.children[j].innerHTML = "".concat((parseFloat(s1s2epsrecap.children[1].innerHTML) / s1s2epsrecap.children[0].innerHTML).toFixed(2), " / 20");
    }

    if (j == 3) {
      var total = parseFloat(s1s2epsrecap.children[1].innerHTML);
      s1s2epsrecap.children[j].innerHTML = "".concat(mydata[7].indexOf(data2[i][13][2]) + 1, "  /  ").concat(data2.length);
    }

    if (j == 4) {
      s1s2epsrecap.children[j].innerHTML = "".concat(sommeInt2(resultat.lastChild.innerHTML, s2epsResult.lastChild.innerHTML), "  /  60");
    }

    if (j == 5) {
      var moyenne = parseFloat(s1s2epsrecap.children[2].innerHTML);

      if (moyenne >= 10) {
        s1s2epsrecap.children[j].innerHTML = "ADMIS(E)";
      } else {
        s1s2epsrecap.children[j].innerHTML = "REFUSE(E)";
      }
    }
  }

  return clone;
}