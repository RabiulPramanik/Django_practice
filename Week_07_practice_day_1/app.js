const loadProducts = () => {
    fetch('https://fakestoreapi.com/products')
    .then(response => response.json())
    .then(data => {
        document.getElementById("product-card").innerHTML = "";
        displayProducts(data);
    });
};
const loadProductsBYcategory = (search) => {
    document.getElementById("product-card").innerHTML = "";
    fetch(`https://fakestoreapi.com/products/category/${search ? search : ""}`)
    .then(response => response.json())
    .then(data => {
        if (data.length > 0){
            displayProducts(data);
        }
        else{
            console.log("data not found!");
        }
    });
};
const displayProducts = (products) =>{
    products.forEach(product => {
        const prant = document.getElementById("product-card")
        const div = document.createElement("div")
        div.classList.add("col")
        div.innerHTML = `
            <div class="card">
            <img class="card-img" src="${product.image}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${product.title}</h5>
                <h6 class="card-title">${product.category}</h6>
                <p class="card-text">${product.description.slice(0, 150)}</p>
                <a target="_blank" href="details.html?productId=${product.id}" class="btn btn-primary">Details</a>
            </div>
            </div>
        `; 
        prant.append(div);
    });
};

const loadCategorys = () => {
    fetch('https://fakestoreapi.com/products/categories')
    .then(response => response.json())
    .then(data => {
        displayCategory(data);
    });
};
const displayCategory = (categorys) =>{
    categorys.forEach(category => {
        const prant = document.getElementById("category-container");
        const li = document.createElement("li")
            li.classList.add("dropdown-item")
            if (category == "men's clothing"){
                li.innerHTML = `
                <li onclick="loadProductsBYcategory('men\'s clothing')"> ${category}</li>
              `;
            }
            else if(category == "women's clothing"){
                li.innerHTML = `
                <li onclick="loadProductsBYcategory('women\'s clothing')"> ${category}</li>
              `;
            }
            else{
                li.innerHTML = `
                <li onclick="loadProductsBYcategory('${category}')"> ${category}</li>
              `;
            }
            prant.append(li);
    });
};
loadProducts();
loadCategorys();




