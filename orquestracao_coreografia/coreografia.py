class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event_type, data):
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                handler(data)

# Inicializando o EventBus
event_bus = EventBus()

class PaymentService:
    def __init__(self, event_bus):
        event_bus.subscribe("order_created", self.process_payment)

    def process_payment(self, order):
        print("Processando pagamento...")
        event_bus.publish("payment_processed", order)

class InventoryService:
    def __init__(self, event_bus):
        event_bus.subscribe("payment_processed", self.update_inventory)

    def update_inventory(self, order):
        print("Atualizando inventário...")
        event_bus.publish("inventory_updated", order)

class NotificationService:
    def __init__(self, event_bus):
        event_bus.subscribe("inventory_updated", self.send_confirmation)

    def send_confirmation(self, order):
        print("Enviando confirmação de pedido...")

# Configurando os serviços e assinando aos eventos
payment_service = PaymentService(event_bus)
inventory_service = InventoryService(event_bus)
notification_service = NotificationService(event_bus)

# Iniciando o fluxo com a criação de um pedido
order = {"id": 123, "itens": ["item1", "item2"]}
event_bus.publish("order_created", order)
