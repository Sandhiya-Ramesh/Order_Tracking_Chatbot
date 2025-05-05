orders = {
    "1234": {"item": "Wireless Mouse", "status": "Shipped", "estimated_delivery": "2025-05-08"},
    "5678": {"item": "Laptop", "status": "Out for Delivery", "estimated_delivery": "2025-05-06"},
    "9101": {"item": "Book", "status": "Delivered", "estimated_delivery": "2025-05-03"},
    "1122": {"item": "Bluetooth Headphones", "status": "Processing", "estimated_delivery": "2025-05-10"},
    "3344": {"item": "Smartphone", "status": "Packed", "estimated_delivery": "2025-05-09"},
    "5566": {"item": "Desk Lamp", "status": "Shipped", "estimated_delivery": "2025-05-07"},
    "7788": {"item": "Keyboard", "status": "Delivered", "estimated_delivery": "2025-05-02"},
    "9900": {"item": "Webcam", "status": "Out for Delivery", "estimated_delivery": "2025-05-06"},
    "2468": {"item": "Tablet", "status": "Cancelled", "estimated_delivery": "N/A"},
    "1357": {"item": "Monitor", "status": "Returned", "estimated_delivery": "N/A"},
}


def get_order_details(order_id):
    return orders.get(order_id)
