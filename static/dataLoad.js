const productData = [];

// Load data for using AJAX call 
function loadDoc() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        var json = JSON.parse(this.responseText);
        json.forEach(p => productData.push(p))
    }
    xhttp.open("GET", "../static/data.json");
    xhttp.send();
}

loadDoc();

// Element to place the chart in 
const productModel = document.getElementById('productModel')

const NutriLabel = ['Calories', 'Protein', 'Fat', 'Sat.Fat', 'Fiber', 'Carbs'];
const colourLabel = ['#F66D44', '#FEAE65', '#E6F69D', '#AADEA7', '#64C2A6', '#2D87BB'];

const doughnutConfig = {
    labels: NutriLabel,
    datasets: [
        {
            label: 'Nutrition Vlaue',
            backgroundColor: colourLabel
        }
    ]
};

const doughnutOptions = {
    responsive: true,
    plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'Nutrition Vlaue'
        }
    }
};

function updateProductModel(event, container) {
    console.log(container.id)

    var pd = productData.find(p => p.id == container.id);
    const modelDiv = `<div class="modal-header">
                        <h3 class="modal-title">${pd.name}</h3>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body productsDetails">
                        <h5 style="text-align: left;">Nutrition chart :-</h3>
                         <canvas id="productChart" style="width:100%;max-width:700px"></canvas>
                        <h5 style="text-align: left;">Price : $ ${pd.price}</h3>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                    </div>`;

    const modalContent = document.querySelector(".modal-content");
    modalContent.innerHTML = modelDiv;

    const data = doughnutConfig;
    data.datasets[0].data = pd.nutriValue
    data.datasets[0].label = pd.name + " Nutri Chart"


    new Chart("productChart", {
        type: "doughnut",
        data: data,
        options: doughnutOptions
    });
}

var myModal = new bootstrap.Modal(productModel, {
    keyboard: false
})

/** Adding Event listener to capture the mouse click over the images */
const containers = document.querySelectorAll(".grid-item-product");
containers.forEach(c => c.addEventListener(
    "click",
    function (event) {
        updateProductModel(event, c)
        myModal.show()
    },
    false
));
