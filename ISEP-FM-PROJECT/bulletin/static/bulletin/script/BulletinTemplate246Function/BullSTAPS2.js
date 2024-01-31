
/**FONCTION BULLETIN STAPS2 */
function sommeInt9(a, b, c, d, e, f, g, h, i) {
    a = parseInt(a);
    b = parseInt(b);
    c = parseInt(c);
    d = parseInt(d);
    e = parseInt(e);
    f = parseInt(f);
    g = parseInt(g);
    h = parseInt(h);
    i = parseInt(i)

    var result = a + b + c + d + e + f + g + h + i
    return (result)
}
function sommeInt2(a, b) {
    a = parseInt(a)
    b = parseInt(b);

    var result = a + b

    return (result)
}

function sommeFloat(a, b, c, d, e, f, g, h) {
    a = parseFloat(a)
    b = parseFloat(b);
    c = parseFloat(c);
    d = parseFloat(d);
    e = parseFloat(e);
    f = parseFloat(f);
    g = parseFloat(g);
    h = parseFloat(h);

    result = a + b + c + d + e + f + g + h + i + j
    result = result.toFixed(2)
    result = parseFloat(result)

    return (result)
}

function sommeFloat2(a, b) {
    a = parseFloat(a)
    b = parseFloat(b);

    var result = a + b
    result = result.toFixed(2)
    result = parseFloat(result)

    return (result)
}

export default function BullSTAPS2(clone, i, mydata) {

    //DONNEES RECUPEREES DE LA BD
    var listStudent = mydata[1]

    //Info Utilisateur
    var info1 = clone.children[2].children[1].children[0]
    info1.children[2].innerHTML = info1.children[2].innerHTML + ` ${listStudent[i][0]['nom']}`
    info1.children[3].innerHTML = info1.children[3].innerHTML + ` ${listStudent[i][0]['prenom']}`

    var info2 = clone.children[2].children[1].children[1]
    info2.children[1].innerHTML = info2.children[1].innerHTML + ` ${listStudent[i][0]['matricule']}`
    info2.children[2].innerHTML = info2.children[2].innerHTML + ` ${listStudent[i][0]['date_naissance']}`
    info2.children[3].innerHTML = info2.children[3].innerHTML + ` ${listStudent[i][0]['lieu_naissance']}`
    info2.children[4].innerHTML = info2.children[4].innerHTML + ` 2022-2023`   //Ajout de la variable  de la date

    //RESULTATS
    var tbody = clone.children[2].children[2].children[0].children[1]

    //LIGNE EPS111
    var ligneEPS111 = tbody.children[0]
    for (var j = 0; j <= ligneEPS111.childElementCount - 1; j++) {
        if (j == 4) { ligneEPS111.children[j].innerHTML = listStudent[i][1][0] } //note 
        if (j == 5) { ligneEPS111.children[j].innerHTML = listStudent[i][1][1] } //coef
        if (j == 6) {
            var val = ligneEPS111.children[4].innerHTML * ligneEPS111.children[5].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS111.children[j].innerHTML = val
        } //total note  * coef
        if (j == 7) { ligneEPS111.children[j].innerHTML = listStudent[i][1][3] } //moyenne donc (totalmath + totalinfo)/2
        if (j == 8) { ligneEPS111.children[j].innerHTML = listStudent[i][1][4] } //Rang
        if (j == 9) {
            // if (((listStudent[i][1][0] >= 7 && listStudent[i][1][0] < 10) && listStudent[i][1][3] >= 10)) { ligneMAS315.children[j].innerHTML = "Validée" } else if ((listStudent[i][1][0] >= 10)) { ligneMAS315.children[j].innerHTML = "Validée" } else if (listStudent[i][1][0] < 10) { ligneMAS315.children[j].innerHTML = "Non validée" }
            if (listStudent[i][1][5]) {
                ligneEPS111.children[j].innerHTML = "Validée"
                ligneEPS111.children[9].innerHTML = "Validée"
            } else { ligneEPS111.children[9].innerHTML = "Non validée" }
        } //Mention
        if (j == 10) { ligneEPS111.children[j].innerHTML = mydata[4] } //Session
        if (j == 11) { if (listStudent[i][1][0] >= 10) { ligneEPS111.children[j].innerHTML = listStudent[i][1][6] } else { ligneEPS111.children[j].innerHTML = 0 } } //Crédits
    }

    //LIGNE EPS112
    var ligneEPS112 = tbody.children[1]
    for (j = 0; j <= ligneEPS112.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS112.children[j].innerHTML = listStudent[i][2][0] } //note info
        if (j == 3) { ligneEPS112.children[j].innerHTML = listStudent[i][2][1] } //coef info
        if (j == 4) { ligneEPS112.children[j].innerHTML = listStudent[i][2][2] } //val=ligneEPS112.children[2].innerHTML*ligneEPS112.children[3].innerHTML; val= val.toFixed(2); val = parseFloat(val); ligneEPS112.children[j].innerHTML = val}//total note math * coef
        if (j == 5) { ligneEPS112.children[j].innerHTML = listStudent[i][2][4] } //Rang
        if (j == 6) {
            if (listStudent[i][2][5]) { ligneEPS112.children[6].innerHTML = "Validée" } else { ligneEPS112.children[6].innerHTML = "Non validée" }
        }
        if (j == 7) { ligneEPS112.children[j].innerHTML = mydata[4] } //Session
        if (j == 8) { if (listStudent[i][2][5]) { ligneEPS112.children[j].innerHTML = listStudent[i][2][6] } else { ligneEPS112.children[j].innerHTML = 0 } } //Crédits
    }

    //LIGNE EPS113
    var ligneEPS113 = tbody.children[2]
    for (j = 0; j <= ligneEPS113.childElementCount - 1; j++) {
        if (j == 3) { ligneEPS113.children[j].innerHTML = listStudent[i][3][0] } //note info
        if (j == 4) { ligneEPS113.children[j].innerHTML = listStudent[i][3][1] } //coef info
        if (j == 5) {
            val = ligneEPS113.children[2].innerHTML * ligneEPS113.children[3].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS113.children[j].innerHTML = listStudent[i][3][2]
        } //total note math * coef
        if (j == 6) { ligneEPS113.children[j].innerHTML = listStudent[i][3][3] } //
        if (j == 7) { ligneEPS113.children[j].innerHTML = listStudent[i][3][4] }
        if (j == 8) { if (listStudent[i][3][5]) { ligneEPS113.children[j].innerHTML = "Validée" } else { ligneEPS113.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 9) { ligneEPS113.children[j].innerHTML = mydata[4] } // Session
        if (j == 10) { if (listStudent[i][3][5]) { ligneEPS113.children[j].innerHTML = listStudent[i][3][6] } else { ligneEPS113.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS114
    var ligneEPS114 = tbody.children[3]
    for (j = 0; j <= ligneEPS114.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS114.children[j].innerHTML = listStudent[i][4][0] } //note info
        if (j == 3) { ligneEPS114.children[j].innerHTML = listStudent[i][4][1] } //coef info
        if (j == 4) { /*val=ligneEPS114.children[2].innerHTML*ligneEPS114.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS114.children[j].innerHTML = listStudent[i][4][2] } //total note math * coef
        if (j == 5) { ligneEPS114.children[j].innerHTML = listStudent[i][4][4] } //
        if (j == 6) { if (listStudent[i][4][5]) { ligneEPS114.children[j].innerHTML = "Validée" } else { ligneEPS114.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS114.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][4][5]) { ligneEPS114.children[j].innerHTML = listStudent[i][4][6] } else { ligneEPS114.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115a
    var ligneEPS115a = tbody.children[4]
    for (j = 0; j <= ligneEPS115a.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][0] } //note info
        if (j == 3) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][1] } //coef info
        if (j == 4) { /*val=ligneEPS115a.children[2].innerHTML*ligneEPS115a.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115a.children[j].innerHTML = listStudent[i][5][2] } //total note math * coef
        if (j == 5) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][4] } //
        if (j == 6) { if (listStudent[i][5][5]) { ligneEPS115a.children[j].innerHTML = "Validée" } else { ligneEPS115a.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115a.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if ((listStudent[i][5][0] + listStudent[i][6][0] + listStudent[i][7][0] + listStudent[i][8][0] + listStudent[i][9][0] + listStudent[i][10][0]) >= 48) { ligneEPS115a.children[j].innerHTML = listStudent[i][5][6] } else { ligneEPS115a.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115b
    var ligneEPS115b = tbody.children[5]
    for (j = 0; j <= ligneEPS115b.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][0] } //note info
        if (j == 3) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][1] } //coef info
        if (j == 4) { /*val=ligneEPS115b.children[2].innerHTML*ligneEPS115b.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115b.children[j].innerHTML = listStudent[i][6][2] } //total note math * coef
        if (j == 5) { ligneEPS115b.children[j].innerHTML = listStudent[i][5][4] } //
        if (j == 6) { if (listStudent[i][6][5]) { ligneEPS115b.children[j].innerHTML = "Validée" } else { ligneEPS115b.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115b.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][6][5]) { ligneEPS115b.children[j].innerHTML = listStudent[i][6][6] } else { ligneEPS115b.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //Ligne EPS115f
    var ligneEPS115f = tbody.children[6]
    for (j = 0; j <= ligneEPS115f.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][0] } //note info
        if (j == 3) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][1] } //coef info
        if (j == 4) { /*val=ligneEPS115f.children[2].innerHTML*ligneEPS115f.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115f.children[j].innerHTML = listStudent[i][7][2] } //total note math * coef
        if (j == 5) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][4] } //
        if (j == 6) { if (listStudent[i][7][5]) { ligneEPS115f.children[j].innerHTML = "Validée" } else { ligneEPS115f.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115f.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][7][5]) { ligneEPS115f.children[j].innerHTML = listStudent[i][7][6] } else { ligneEPS115f.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //Ligne EPS115g
    var ligneEPS115g = tbody.children[7]
    for (j = 0; j <= ligneEPS115g.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][0] } //note info
        if (j == 3) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][1] } //coef info
        if (j == 4) { /*val=ligneEPS115g.children[2].innerHTML*ligneEPS115g.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115g.children[j].innerHTML = listStudent[i][8][2] } //total note math * coef
        if (j == 5) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][4] } //
        if (j == 6) { if (listStudent[i][8][5]) { ligneEPS115g.children[j].innerHTML = "Validée" } else { ligneEPS115g.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115g.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][8][5]) { ligneEPS115g.children[j].innerHTML = listStudent[i][8][6] } else { ligneEPS115g.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115j
    var ligneEPS115j = tbody.children[8]
    for (j = 0; j <= ligneEPS115j.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][0] } //note info
        if (j == 3) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][1] } //coef info
        if (j == 4) { /*val=ligneEPS115j.children[2].innerHTML*ligneEPS115j.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115j.children[j].innerHTML = listStudent[i][9][2] } //total note math * coef
        if (j == 5) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][4] } //
        if (j == 6) { if (listStudent[i][9][5]) { ligneEPS115j.children[j].innerHTML = "Validée" } else { ligneEPS115j.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115j.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][9][5]) { ligneEPS115j.children[j].innerHTML = listStudent[i][9][6] } else { ligneEPS115j.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS115l
    var ligneEPS115l = tbody.children[9]
    for (j = 0; j <= ligneEPS115l.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][0] } //note info
        if (j == 3) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][1] } //coef info
        if (j == 4) { /*val=ligneEPS115l.children[2].innerHTML*ligneEPS115l.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS115l.children[j].innerHTML = listStudent[i][10][2] } //total note math * coef
        if (j == 5) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][4] } //
        if (j == 6) { if (listStudent[i][10][5]) { ligneEPS115l.children[j].innerHTML = "Validée" } else { ligneEPS115l.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS115l.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][10][5]) { ligneEPS115l.children[j].innerHTML = listStudent[i][10][6] } else { ligneEPS115l.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS116
    var ligneEPS116 = tbody.children[10]
    for (j = 0; j <= ligneEPS116.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS116.children[j].innerHTML = listStudent[i][11][0] } //note info
        if (j == 3) { ligneEPS116.children[j].innerHTML = listStudent[i][11][1] } //coef info
        if (j == 4) { /*val=ligneEPS116.children[2].innerHTML*ligneEPS116.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS116.children[j].innerHTML = listStudent[i][11][2] } //total note math * coef
        if (j == 5) { ligneEPS116.children[j].innerHTML = listStudent[i][9][4] } //
        if (j == 6) { if (listStudent[i][11][5]) { ligneEPS116.children[j].innerHTML = "Validée" } else { ligneEPS116.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS116.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][11][5]) { ligneEPS116.children[j].innerHTML = listStudent[i][11][6] } else { ligneEPS116.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS117
    var ligneEPS117 = tbody.children[11]
    for (j = 0; j <= ligneEPS117.childElementCount - 1; j++) {
        if (j == 3) { ligneEPS117.children[j].innerHTML = listStudent[i][12][0] } //note info
        if (j == 4) { ligneEPS117.children[j].innerHTML = listStudent[i][12][1] } //coef info
        if (j == 5) {
            val = ligneEPS117.children[2].innerHTML * ligneEPS117.children[3].innerHTML;
            val = val.toFixed(2);
            val = parseFloat(val);
            ligneEPS117.children[j].innerHTML = listStudent[i][12][2]
        } //total note math * coef
        if (j == 6) { ligneEPS117.children[j].innerHTML = listStudent[i][12][3] } //
        if (j == 7) { ligneEPS117.children[j].innerHTML = listStudent[i][12][4] }
        if (j == 8) { if (listStudent[i][12][5]) { ligneEPS117.children[j].innerHTML = "Validée" } else { ligneEPS117.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 9) { ligneEPS117.children[j].innerHTML = mydata[4] } // Session
        if (j == 10) { if (listStudent[i][12][5]) { ligneEPS117.children[j].innerHTML = listStudent[i][12][6] } else { ligneEPS117.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS118
    var ligneEPS118 = tbody.children[12]
    for (j = 0; j <= ligneEPS118.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS118.children[j].innerHTML = listStudent[i][13][0] } //note info
        if (j == 3) { ligneEPS118.children[j].innerHTML = listStudent[i][13][1] } //coef info
        if (j == 4) { /*val=ligneEPS118.children[2].innerHTML*ligneEPS118.children[3].innerHTML; val=val.toFixed(2); val=parseFloat(val);*/ ligneEPS118.children[j].innerHTML = listStudent[i][13][2] } //total note math * coef
        if (j == 5) { ligneEPS118.children[j].innerHTML = listStudent[i][13][4] } //
        if (j == 6) { if (listStudent[i][13][5]) { ligneEPS118.children[j].innerHTML = "Validée" } else { ligneEPS118.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS118.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][13][5]) { ligneEPS118.children[j].innerHTML = listStudent[i][13][6] } else { ligneEPS118.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LIGNE EPS119
    var ligneEPS119 = tbody.children[13]
    for (j = 0; j <= ligneEPS119.childElementCount - 1; j++) {
        if (j == 2) { ligneEPS119.children[j].innerHTML = listStudent[i][14][0] } //note info
        if (j == 3) { ligneEPS119.children[j].innerHTML = listStudent[i][14][1] } //coef info
        if (j == 4) { ligneEPS119.children[j].innerHTML = listStudent[i][14][2] } //total note math * coef
        if (j == 5) { ligneEPS119.children[j].innerHTML = listStudent[i][14][4] } //
        if (j == 6) { if (listStudent[i][14][5]) { ligneEPS119.children[j].innerHTML = "Validée" } else { ligneEPS119.children[j].innerHTML = "Non validée" } } //Mention
        if (j == 7) { ligneEPS119.children[j].innerHTML = mydata[4] } //session
        if (j == 8) { if (listStudent[i][14][5]) { ligneEPS119.children[j].innerHTML = listStudent[i][14][6] } else { ligneEPS119.children[j].innerHTML = 0 } } //nombre_crédits
    }

    //LINE DEs RESULTATS
    var resultat = tbody.children[14]
    for (j = 0; j <= resultat.childElementCount - 1; j++) {
        if (j == 1) {
            resultat.children[1].innerHTML = listStudent[i][15][0];
        }
        if (j == 2) { resultat.children[2].innerHTML = listStudent[i][15][1] }
        if (j == 3) { resultat.children[j].innerHTML = listStudent[i][15][2] }
        if (j == 4) { resultat.children[j].innerHTML = mydata[2].indexOf(listStudent[i][15][2]) + 1 }
        if (j == 6) { resultat.children[6].innerHTML = sommeInt9(ligneEPS111.children[11].innerHTML, ligneEPS112.children[8].innerHTML, ligneEPS113.children[10].innerHTML, ligneEPS114.children[8].innerHTML, ligneEPS115a.children[8].innerHTML, ligneEPS116.children[8].innerHTML, ligneEPS117.children[10].innerHTML, ligneEPS118.children[8].innerHTML, ligneEPS119.children[8].innerHTML) }
    }

    //Tbody
    var body3 = clone.children[2].children[2].children[1].children[1]

    //LIGNE 0
    var ligne0 = body3.children[0]
    for (j = 0; j <= ligne0.childElementCount - 1; j++) {
        if (j == 2) { ligne0.children[2].innerHTML = `${ listStudent[i][15][2] } / 20` }
        if (j == 4) { ligne0.children[j].innerHTML = `${mydata[2][0]} / 20` }
    }

    //LIGNE 1
    var ligne1 = body3.children[1]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 2) { ligne1.children[j].innerHTML = `${mydata[3]} / 20` }
        if (j == 4) {
            var note_length = mydata[2].length - 1;
            ligne1.children[j].innerHTML = `${mydata[2][note_length]} / 20`
        } //
    }

    //LLIGNE 2
    var ligne2 = body3.children[2]
    for (j = 0; j <= ligne1.childElementCount - 1; j++) {
        if (j == 5) { ligne2.children[j].innerHTML = `${resultat.children[4].innerHTML} sur ${mydata[1].length}` }
        if (j == 4) {}
    }
    resultat.style.backgroundColor = "#C7B54D"

    // ##################### SEMESTRE 4 ###################################################################################
    var listStudent2 = mydata[10][0]
    var s4body = clone.children[2].children[3].children[0].children[1]

    //Ligne 3
    var ligne33 = s4body.children[2]
    for (var j = 0; j <= ligne33.childElementCount - 1; j++) {
        if (j == 3) { ligne33.children[j].innerHTML = listStudent2[i][1][0] }
        if (j == 4) { ligne33.children[j].innerHTML = listStudent2[i][1][1] }
        if (j == 5) { ligne33.children[j].innerHTML = listStudent2[i][1][2] }
        if (j == 6) { ligne33.children[j].innerHTML = listStudent2[i][10][3] }
        if (j == 7) { ligne33.children[j].innerHTML = listStudent2[i][1][4] }
        if (j == 8) {
            if (listStudent2[i][1][5]) { ligne33.children[j].innerHTML = 'Validée' } else {
                ligne33.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 9) {
            if (listStudent2[i][1][10]) { ligne33.children[j].innerHTML = "Rattrapage" } else { ligne33.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 10) { ligne33.children[j].innerHTML = listStudent2[i][1][7] }
    }
    //Ligne 4
    var ligne44 = s4body.children[3]
    for (j = 0; j <= ligne44.childElementCount - 1; j++) {
        if (j == 2) { ligne44.children[j].innerHTML = listStudent2[i][2][0] }
        if (j == 3) { ligne44.children[j].innerHTML = listStudent2[i][2][1] }
        if (j == 4) { ligne44.children[j].innerHTML = listStudent2[i][2][2] }
        if (j == 5) { ligne44.children[j].innerHTML = listStudent2[i][2][4] }
        if (j == 6) {
            if (listStudent2[i][2][5]) { ligne44.children[j].innerHTML = 'Validée' } else {
                ligne44.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][2][10]) { ligne44.children[j].innerHTML = "Rattrapage" } else { ligne44.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne44.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 5
    var ligne55 = s4body.children[4]
    for (j = 0; j <= ligne55.childElementCount - 1; j++) {
        if (j == 2) { ligne55.children[j].innerHTML = listStudent2[i][3][0] }
        if (j == 3) { ligne55.children[j].innerHTML = listStudent2[i][3][1] }
        if (j == 4) { ligne55.children[j].innerHTML = listStudent2[i][3][2] }
        if (j == 5) { ligne55.children[j].innerHTML = listStudent2[i][3][4] }
        if (j == 6) {
            if (listStudent2[i][3][5]) { ligne55.children[j].innerHTML = 'Validée' } else {
                ligne55.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][3][10]) { ligne55.children[j].innerHTML = "Rattrapage" } else { ligne55.children[j].innerHTML = "Mai 2023" }
        }
        //if (j == 8) { ligne55.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 6
    var ligne66 = s4body.children[5]
    for (j = 0; j <= ligne66.childElementCount - 1; j++) {
        if (j == 2) { ligne66.children[j].innerHTML = listStudent2[i][4][0] }
        if (j == 3) { ligne66.children[j].innerHTML = listStudent2[i][4][1] }
        if (j == 4) { ligne66.children[j].innerHTML = listStudent2[i][4][2] }
        if (j == 5) { ligne66.children[j].innerHTML = listStudent2[i][4][4] }
        if (j == 6) {
            if (listStudent2[i][4][5]) { ligne66.children[j].innerHTML = 'Validée' } else {
                ligne66.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][4][10]) { ligne66.children[j].innerHTML = "Rattrapage" } else { ligne66.children[j].innerHTML = "Mai 2023" }
        }
        //if (j == 8) { ligne55.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 7
    var ligne77 = s4body.children[6]
    for (j = 0; j <= ligne77.childElementCount - 1; j++) {
        if (j == 2) { ligne77.children[j].innerHTML = listStudent2[i][5][0] }
        if (j == 3) { ligne77.children[j].innerHTML = listStudent2[i][5][1] }
        if (j == 4) { ligne77.children[j].innerHTML = listStudent2[i][5][2] }
        if (j == 5) { ligne77.children[j].innerHTML = listStudent2[i][5][4] }
        if (j == 6) {
            if (listStudent2[i][5][5]) { ligne77.children[j].innerHTML = 'Validée' } else {
                ligne77.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][5][10]) { ligne77.children[j].innerHTML = "Rattrapage" } else { ligne77.children[j].innerHTML = "Mai 2023" }
        }
        //if (j == 8) { ligne55.children[j].innerHTML = listStudent2[i][2][7] }
    }

    //Ligne 8
    var ligne88 = s4body.children[7]
    for (j = 0; j <= ligne88.childElementCount - 1; j++) {
        if (j == 2) { ligne88.children[j].innerHTML = listStudent2[i][6][0] }
        if (j == 3) { ligne88.children[j].innerHTML = listStudent2[i][6][1] }
        if (j == 4) { ligne88.children[j].innerHTML = listStudent2[i][6][2] }
        if (j == 5) { ligne88.children[j].innerHTML = listStudent2[i][6][4] }
        if (j == 6) {
            if (listStudent2[i][6][5]) { ligne88.children[j].innerHTML = 'Validée' } else {
                ligne88.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][6][10]) { ligne88.children[j].innerHTML = "Rattrapage" } else { ligne88.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne88.children[j].innerHTML = listStudent2[i][6][7] }
    }
    //Ligne 9
    var lignee99 = s4body.children[8]
    for (j = 0; j <= lignee99.childElementCount - 1; j++) {
        if (j == 2) { lignee99.children[j].innerHTML = listStudent2[i][7][0] }
        if (j == 3) { lignee99.children[j].innerHTML = listStudent2[i][7][1] }
        if (j == 4) { lignee99.children[j].innerHTML = listStudent2[i][7][2] }
        if (j == 5) { lignee99.children[j].innerHTML = listStudent2[i][7][4] }
        if (j == 6) {
            if (listStudent2[i][7][5]) { lignee99.children[j].innerHTML = 'Validée' } else {
                lignee99.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][7][10]) { lignee99.children[j].innerHTML = "Rattrapage" } else { lignee99.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { lignee99.children[j].innerHTML = listStudent2[i][7][7] }
    }
    //Ligne 10
    var ligne10 = s4body.children[9]
    for (j = 0; j <= ligne10.childElementCount - 1; j++) {
        if (j == 2) { ligne10.children[j].innerHTML = listStudent2[i][8][0] }
        if (j == 3) { ligne10.children[j].innerHTML = listStudent2[i][8][1] }
        if (j == 4) { ligne10.children[j].innerHTML = listStudent2[i][8][2] }
        if (j == 5) { ligne10.children[j].innerHTML = listStudent2[i][8][4] }
        if (j == 6) {
            if (listStudent2[i][8][5]) { ligne10.children[j].innerHTML = 'Validée' } else {
                ligne10.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][8][10]) { ligne10.children[j].innerHTML = "Rattrapage" } else { ligne10.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne10.children[j].innerHTML = listStudent2[i][8][7] }
    }

    //Ligne 11
    var ligne11 = s4body.children[10]
    for (j = 0; j <= ligne11.childElementCount - 1; j++) {
        if (j == 2) { ligne11.children[j].innerHTML = listStudent2[i][9][0] }
        if (j == 3) { ligne11.children[j].innerHTML = listStudent2[i][9][1] }
        if (j == 4) { ligne11.children[j].innerHTML = listStudent2[i][9][2] }
        if (j == 5) { ligne11.children[j].innerHTML = listStudent2[i][9][4] }
        if (j == 6) {
            if (listStudent2[i][9][5]) { ligne11.children[j].innerHTML = 'Validée' } else {
                ligne11.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][9][10]) { ligne11.children[j].innerHTML = "Rattrapage" } else { ligne11.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne11.children[j].innerHTML = listStudent2[i][9][7] }
    }

    //Ligne 12
    var ligne12 = s4body.children[11]
    for (j = 0; j <= ligne12.childElementCount - 1; j++) {
        if (j == 2) { ligne12.children[j].innerHTML = listStudent2[i][10][0] }
        if (j == 3) { ligne12.children[j].innerHTML = listStudent2[i][10][1] }
        if (j == 4) { ligne12.children[j].innerHTML = listStudent2[i][10][2] }
        if (j == 5) { ligne12.children[j].innerHTML = listStudent2[i][10][4] }
        if (j == 6) {
            if (listStudent2[i][10][5]) { ligne12.children[j].innerHTML = 'Validée' } else {
                ligne12.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][10][10]) { ligne12.children[j].innerHTML = "Rattrapage" } else { ligne12.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne12.children[j].innerHTML = listStudent2[i][10][7] }
    }

    //Ligne 13
    var ligne13 = s4body.children[12]
    for (j = 0; j <= ligne13.childElementCount - 1; j++) {
        if (j == 3) { ligne13.children[j].innerHTML = listStudent2[i][11][0] }
        if (j == 4) { ligne13.children[j].innerHTML = listStudent2[i][11][1] }
        if (j == 5) { ligne13.children[j].innerHTML = listStudent2[i][11][2] }
        if (j == 6) { ligne13.children[j].innerHTML = listStudent2[i][12][3] }
        if (j == 7) { ligne13.children[j].innerHTML = listStudent2[i][11][4] }
        if (j == 8) {
            if (listStudent2[i][11][5]) { ligne13.children[j].innerHTML = 'Validée' } else {
                ligne13.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 9) {
            if (listStudent2[i][11][10]) { ligne13.children[j].innerHTML = "Rattrapage" } else { ligne13.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 10) { ligne13.children[j].innerHTML = listStudent2[i][11][7] }

    }

    //Ligne 14
    var ligne14 = s4body.children[13]
    for (j = 0; j <= ligne14.childElementCount - 1; j++) {
        if (j == 2) { ligne14.children[j].innerHTML = listStudent2[i][12][0] }
        if (j == 3) { ligne14.children[j].innerHTML = listStudent2[i][12][1] }
        if (j == 4) { ligne14.children[j].innerHTML = listStudent2[i][12][2] }
        if (j == 5) { ligne14.children[j].innerHTML = listStudent2[i][12][4] }
        if (j == 6) {
            if (listStudent2[i][12][5]) { ligne14.children[j].innerHTML = 'Validée' } else {
                ligne14.children[j].innerHTML = 'Non validée'
            }
        }
        if (j == 7) {
            if (listStudent2[i][12][10]) { ligne14.children[j].innerHTML = "Rattrapage" } else { ligne14.children[j].innerHTML = "Mai 2023" }
        }
        if (j == 8) { ligne14.children[j].innerHTML = listStudent2[i][12][7] }

    }

    //Ligne 16 
    /*var*/
    var ligne16 = s4body.children[15]
    ligne16.style.backgroundColor = 'rgb(199, 181, 77)'
    for (j = 0; j <= 6; j++) {
        //if (j == 0) { ligne16.children[j].innerHTML = "" }
        if (j == 1) { ligne16.children[j].innerHTML = listStudent2[i][13][0] }
        if (j == 2) { ligne16.children[j].innerHTML = listStudent2[i][13][1] }
        if (j == 3) { ligne16.children[j].innerHTML = listStudent2[i][13][2] }
        if (j == 4) { ligne16.children[j].innerHTML = mydata[10][1].indexOf(listStudent2[i][13][2]) + 1 }
        //if (j == 5) { ligne16.children[j].innerHTML = "OBOSSO" }
        if (j == 6) {
            ligne16.children[j].innerHTML = sommeInt9(ligne33.lastChild.innerHTML, ligne44.lastChild.innerHTML, ligne88.lastChild.innerHTML, lignee99.lastChild.innerHTML, ligne10.lastChild.innerHTML, ligne11.lastChild.innerHTML, ligne12.lastChild.innerHTML, ligne13.lastChild.innerHTML, ligne14.lastChild.innerHTML)
        }
    }

    // SEMESTRE 4 & 3 RESULT
    var resultats4s3 = clone.children[2].children[4]

    var ligneresultat = resultats4s3.children[1].children[1]

    for (j = 0; j <= ligneresultat.childElementCount - 1; j++) {
        if (j == 0) { ligneresultat.children[j].innerHTML = sommeInt2(resultat.children[1].innerHTML, ligne16.children[1].innerHTML) }
        if (j == 1) { ligneresultat.children[j].innerHTML = sommeFloat2(resultat.children[2].innerHTML, ligne16.children[2].innerHTML) }
        if (j == 2) { ligneresultat.children[j].innerHTML = `${(parseFloat(ligneresultat.children[1].innerHTML) / ligneresultat.children[0].innerHTML).toFixed(2)} / 20` }
        if (j == 3) {
            var total = parseFloat(ligneresultat.children[1].innerHTML)
            ligneresultat.children[j].innerHTML = `${mydata[10][2].indexOf(total) + 1}  /  ${listStudent2.length}`
        }
        if (j == 4) { ligneresultat.children[j].innerHTML = `${ sommeInt2(resultat.lastChild.innerHTML, ligne16.lastChild.innerHTML) }  /  60` }
        if (j == 5) {
            var moyenne = parseFloat(ligneresultat.children[2].innerHTML)
            if (moyenne >= 10) { ligneresultat.children[j].innerHTML = "ADMIS(E)" } else { ligneresultat.children[j].innerHTML = "ECHEC" }
        }
    }







    return clone
}