from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    "category" : [
      {
        "id": 1,
        "title": "Electronics",
        "subtitle": "Gadgets, audio & more",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Electronics"
      },
      {
        "id": 2,
        "title": "Fashion",
        "subtitle": "Clothes, shoes & accessories",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Fashion"
      },
      {
        "id": 3,
        "title": "Home & Kitchen",
        "subtitle": "Cookware, decor & appliances",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Home+%26+Kitchen"
      },
      {
        "id": 4,
        "title": "Beauty & Care",
        "subtitle": "Skincare, makeup & more",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Beauty+%26+Care"
      },
      {
        "id": 5,
        "title": "Sports",
        "subtitle": "Gear, equipment & fitness",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Sports"
      },
      {
        "id": 6,
        "title": "Toys & Games",
        "subtitle": "Fun for all ages",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Toys+%26+Games"
      },
      {
        "id": 7,
        "title": "Groceries",
        "subtitle": "Daily essentials & food items",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Groceries"
      },
      {
        "id": 8,
        "title": "Mobile Phones",
        "subtitle": "Smartphones & accessories",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Mobile+Phones"
      },
      {
        "id": 9,
        "title": "Furniture",
        "subtitle": "Chairs, sofas & tables",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Furniture"
      },
      {
        "id": 10,
        "title": "Books",
        "subtitle": "Novels, study materials & more",
        "image": "https://dummyimage.com/300x300/cccccc/000000&text=Books"
      }
    ],
    "featured" : [
  {
    "id": 1,
    "name": "Product 1",
    "price": 29.99,
    "image": "https://dummyimage.com/300x300/cccccc/000000&text=Books",
    "view_link": "product.html",
    "add_link": "cart.html"
  },
  {
    "id": 2,
    "name": "Product 2",
    "price": 49.99,
    "image": "https://dummyimage.com/300x300/cccccc/000000&text=Books",
    "view_link": "product.html",
    "add_link": "cart.html"
  },
  {
    "id": 3,
    "name": "Product 3",
    "price": 19.99,
    "image": "https://dummyimage.com/300x300/cccccc/000000&text=Books",
    "view_link": "product.html",
    "add_link": "cart.html"
  },
  {
    "id": 4,
    "name": "Product 4",
    "price": 39.99,
    "image": "https://dummyimage.com/300x300/cccccc/000000&text=Books",
    "view_link": "product.html",
    "add_link": "cart.html"
  }
]


  }
  return render(request, 'index.html', context)

def product(request):
    return render(request, 'product.html')

def cart(request):
    cartItem = [
      {
        "id": 1,
        "name": "Wireless Headphones",
        "description": "Bluetooth over-ear headphones",
        "price": 59.99,
        "quantity": 1,
        "total": 59.99,
        "image": "https://via.placeholder.com/120?text=Headphones"
      },
      {
        "id": 2,
        "name": "Smart Fitness Watch",
        "description": "Heart-rate & activity tracker",
        "price": 79.50,
        "quantity": 1,
        "total": 79.50,
        "image": "https://via.placeholder.com/120?text=Watch"
      },
      {
        "id": 3,
        "name": "Portable Speaker",
        "description": "Compact waterproof speaker",
        "price": 34.99,
        "quantity": 1,
        "total": 34.99,
        "image": "https://via.placeholder.com/120?text=Speaker"
      },
      {
        "id": 4,
        "name": "Digital Keyboard",
        "description": "61-key electronic piano",
        "price": 129.00,
        "quantity": 1,
        "total": 129.00,
        "image": "https://via.placeholder.com/120?text=Keyboard"
      },
      {
        "id": 5,
        "name": "Gaming Mouse",
        "description": "RGB ergonomic gaming mouse",
        "price": 24.99,
        "quantity": 1,
        "total": 24.99,
        "image": "https://via.placeholder.com/120?text=Mouse"
      }
    ]


    return render(request, 'cart.html', {'cartItem': cartItem})

def checkout(request):
    return render(request, 'checkout.html')

