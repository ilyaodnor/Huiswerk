var drank = ['fris', 'bier', 'wijn'];
var eten = [];
var prijzen = {
    fris: 2.00,
    bier: 2.50,
    wijn: 3.00,
    bitterballen_8: 5.00,
    bitterballen_16: 9.00
};

var bestelling = {
    fris: 0,
    bier: 0,
    wijn: 0,
    bitterballen_8: 0,
    bitterballen_16: 0
};
function toonRekening(rekeningText) {
    document.getElementById('rekening').innerText = rekeningText;
}

function start_bestelling(){
    while (true) {
    
        var keuze = prompt("Welke bestelling wilt u toevoegen? (fris/bier/wijn/snack) of 'stop' :");

        if (keuze === 'stop') {
            rekening();
            break;
        }else if(keuze === null){
            document.write('Je hebt niets bestelt')
            break
        }


        if (keuze === 'fris' || keuze === 'bier' || keuze === 'wijn') {
            var aantal = parseInt(prompt(`Hoeveel ${keuze} wilt u toevoegen aan uw bestelling?`), 10);
            
            if (!isNaN(aantal) && aantal > 0) {
                bestelling[keuze] += aantal;
                alert(`U heeft ${aantal} ${keuze} toegevoegd aan uw bestelling.`);
            } else {
                alert("Ongeldig aantal. Probeer opnieuw.");
            }
        
        } else if (keuze === 'snack') {
            var aantalBitterballen = parseInt(prompt("Hoeveel bitterballen wilt u toevoegen? (8 of 16)"), 10);

            if (aantalBitterballen === 8 || aantalBitterballen === 16) {
                var aantalSchalen = parseInt(prompt(`Hoeveel bitterbalschalen van ${aantalBitterballen} stuks wilt u bestellen?`), 10);

                if (!isNaN(aantalSchalen) && aantalSchalen > 0) {
                    if (aantalBitterballen === 8) {
                        bestelling['bitterballen_8'] += aantalSchalen;
                    } else {
                        bestelling['bitterballen_16'] += aantalSchalen;
                    }
                    alert(`U heeft ${aantalSchalen} schalen met ${aantalBitterballen} bitterballen toegevoegd.`);
                } else {
                    alert("Ongeldig aantal schalen. Probeer opnieuw.");
                }
            } else {
                alert("U kunt alleen 8 of 16 bitterballen bestellen. Probeer opnieuw.");
            }
    
        } else {
            alert("U heeft een ongeldige invoer gedaan. Uw bestelling kan niet worden toegevoegd.");
        }
    }



function rekening(){
    totaal = 0
    var rekening = 'Uw rekening:\n'
    
    for(var item in bestelling){
        if (bestelling[item]>0){
            var prijs = prijzen[item] * bestelling[item];
            totaal+=prijs
            rekening += `${ item.replace('_',' ')}:    ${bestelling[item]} * €${prijzen[item]} = €${bestelling[item]*prijzen[item]}\n`
        }
 
    }
    rekening += `\nTotaal € ${totaal.toFixed(2)}`
    document.write(rekening)



}
}


document.getElementById('bestellingButton').addEventListener('click', start_bestelling);

