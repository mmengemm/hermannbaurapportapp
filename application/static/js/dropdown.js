kunden_select = document.getElementById('kunde');
        baustellen_select = document.getElementById('baustelle');

        kunden_select.onchange = function(){
            kunde = kunden_select.value;

            fetch('baustelle/'+ kunde).then(function(response){
                response.json().then(function(data){
                    optionHTML = '';
                    for (baustelle of data.getbaustelle){
                        optionHTML += '<option value="' + baustelle.id + '">' + baustelle.baustelle + '</option>'
                    }
                    baustellen_select.innerHTML = optionHTML;
                });
            });
        }