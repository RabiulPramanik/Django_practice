const getparams = () =>{
    const param = new URLSearchParams(window.location.search).get("productId");
    fetch(`https://fakestoreapi.com/products/${param ? param : ""}`)
      .then((res) => res.json())
      .then((data) =>{
        const prant = document.getElementById("product-details")
        const div = document.createElement("div")
        div.classList.add("card", "mb-3");
        div.innerHTML = `
            <div class="row g-3">
              <div class="col-md-4">
                <img src="${data.image}" class="img-fluid rounded-start" alt="...">
              </div>
              <div class="col-md-8">
                <div class="card-body">
                  <h2 class="card-title">${data.title}</h2>
                  <h6 class="card-title">${data.category}</h6>
                  <p class="card-text">${data.description}</p>
                  <h3 class="card-title">Price: ${data.price}$</h3>
                  <h1 class="card-title">Rating: ${data.rating.rate}</h1>
                </div>
              </div>
            </div>
        `;
        prant.append(div);
      });
};
getparams();