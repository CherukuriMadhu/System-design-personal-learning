"""Builder Pattern 
Definition

The Builder Pattern is used to construct complex objects step-by-step.

It is especially useful when an object has:

Many attributes
Optional attributes
Different combinations of attributes
Real-world example

Consider creating a Computer.

A computer can have:

CPU
RAM
Storage
GPU
Keyboard
Mouse
WiFi
Bluetooth

Some are mandatory and some are optional.

Before Builder ❌"""
class Computer:

    def __init__(
        self,
        cpu,
        ram,
        storage,
        gpu,
        keyboard,
        mouse,
        wifi,
        bluetooth
    ):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.keyboard = keyboard
        self.mouse = mouse
        self.wifi = wifi
        self.bluetooth = bluetooth
"""
Creating it:

computer = Computer(
    "Intel i7",
    "16GB",
    "1TB SSD",
    "RTX 4060",
    True,
    True,
    True,
    True
)
Problem

It's difficult to understand:

"Intel i7",
"16GB",
"1TB SSD",
"RTX 4060"

Which argument represents what?

Also, if there are 15 optional parameters, the constructor becomes ugly.

After Builder ✅"""
class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.keyboard = False
        self.mouse = False
        self.wifi = False
        self.bluetooth = False

    def show(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("GPU:", self.gpu)
        print("Keyboard:", self.keyboard)
        print("Mouse:", self.mouse)
        print("WiFi:", self.wifi)
        print("Bluetooth:", self.bluetooth)


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def add_keyboard(self):
        self.computer.keyboard = True
        return self

    def add_mouse(self):
        self.computer.mouse = True
        return self

    def add_wifi(self):
        self.computer.wifi = True
        return self

    def add_bluetooth(self):
        self.computer.bluetooth = True
        return self

    def build(self):
        return self.computer
"""
Now:
"""
computer = (
    ComputerBuilder()
    .set_cpu("Intel i7")
    .set_ram("16GB")
    .set_storage("1TB SSD")
    .set_gpu("RTX 4060")
    .add_keyboard()
    .add_mouse()
    .add_wifi()
    .build()
)

computer.show()
"""
Much easier to understand.

The important idea

Builder gives us:

Builder
   ↓
Step 1
   ↓
Step 2
   ↓
Step 3
   ↓
build()
   ↓
Object
Real-world examples

Builder is commonly useful for:

Computer configuration
Pizza
HTTP Request
SQL Query
Car
House
User profile
Interview definition

Builder Pattern separates the construction of a complex object from its representation and allows the object to be constructed step-by-step."""