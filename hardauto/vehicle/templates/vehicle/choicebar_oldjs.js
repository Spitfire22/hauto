
    let select_make = document.querySelector('#select_make');
    let select_model = document.querySelector('#select_model');
    let select_system = document.querySelector('#select_system');
    let select_part = document.querySelector('#select_part');
    let select_manufacturedpart = document.querySelector('#select_manufacturedpart')

    select_make.oninput = function() {
        let make_id = select_make.options[select_make.selectedIndex].value;
        http_get("{% url 'vehicle:getmodels' %}?make_id="+make_id, function (data) {
            select_model.style.display = 'block';
            while (select_model.firstChild) {
                select_model.removeChild(select_model.firstChild);
            }
            for (let i=0; i<data.models.length; ++i) {
                let option = document.createElement('option');
                option.value = data.models[i].id;
                option.innerText = data.models[i].name;
                select_model.appendChild(option);
            }
            select_model.oninput();
        });
    };

    select_model.oninput = function() {
        let model_id = select_model.options[select_model.selectedIndex].value;
        http_get("{% url 'vehicle:getsystems' %}?model_id="+model_id, function (data){
            select_system.style.display = 'block';
            while (select_system.firstChild) {
                select_system.removeChild(select_system.firstChild);
            }
            for (let i=0; i<data.systems.length; ++i) {
                let option = document.createElement('option');
                option.value = data.systems[i].id;
                option.innerText = data.systems[i].name;
                select_system.appendChild(option);
            }
        });
    };

    select_system.oninput = function() {
        let system_id = select_system.options[select_system.selectedIndex].value;
        http_get("{% url 'vehicle:getparts' %}?system_id="+system_id, function (data){
            console.log(data);
            select_part.style.display = 'block';
            while (select_part.firstChild) {
                select_part.removeChild(select_part.firstChild);
            }
            for (let i=0; i<data.parts.length; ++i) {
                let option = document.createElement('option');
                option.value = data.parts[i].id;
                option.innerText = data.parts[i].name;
                select_part.appendChild(option);
            }
        });
    };

    select_system.oninput = function() {
        let part_id = select_part.options[select_part.selectedIndex].value;
        http_get("{% url 'vehicle:getmanufacturedparts' %}?part_id="+part_id, function (data) {
            console.log(data);
            select_manufacturedpart.style.display = 'block';
            while (select_manufacturedpart.firstChild) {
                select_manufacturedpart.removeChild(select_manufacturedpart.firstChild);
            }
            for (let i=0; i<data.manufacturedparts.length; ++i) {
                let option = document.createElement('option');
                option.value = data.manufacturedparts[i].id;
                option.innerText = data.manufacturedparts[i].name + ' (' + data.parts[i].manufacturer + ')';
                select_part.appendChild(option);
            }
        });
    };
