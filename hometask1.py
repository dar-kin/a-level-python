from enum import Enum


# Enumeration, representing states
class State(Enum):
    LIQUID = "Liquid"
    GAS = "Gas"
    SOLID = "Solid"


# Enumeration, representing scale types
class Scale(Enum):
    CELSIUS = "Celsius"
    KELVIN = "Kelvin"
    FARENHEIT = "farenheit"


# Base elements class
class Element(object):
    curr_temp = 0
    curr_scale = Scale.CELSIUS
    curr_state = State.LIQUID
    freeze_temp = 0
    boil_temp = 0

    # Function, which accepts temperature value and return element state, after adding this value
    def agg_state(self, t):
        temp = 0
        freeze = 0
        boil = 0
        if self.curr_scale == Scale.FARENHEIT:
            temp = self.from_farenheit_to_celsius(self.curr_temp) + t
            freeze = self.from_farenheit_to_celsius(self.freeze_temp)
            boil = self.from_farenheit_to_celsius(self.boil_temp)
        else:
            temp = self.curr_temp + t
            freeze = self.freeze_temp
            boil = self.boil_temp
        print(f"Adding {t} celsius.")
        print(f"Current temperature is {temp} celsius")
        if temp < freeze:
            return self.curr_state.SOLID
        elif freeze <= temp < boil:
            return self.curr_state.LIQUID
        else:
            return self.curr_state.GAS

    def from_celsius_to_farenheit(self, t):
        return (t * 9 / 5) + 32

    def from_celsius_to_kelvin(self, t):
        return t + 273.15

    def from_farenheit_to_celsius(self, t):
        return (t - 32) * 5 / 9

    def from_farenheit_to_kelvin(self, t):
        return (t - 32) * 5 / 9 + 273.5

    def from_kelvin_to_celsius(self, t):
        return t - 273.5

    def from_kelvin_to_farenheit(self, t):
        return (t - 273.5) * 9 / 5 + 32

    # Function, which swaps scale type
    def swap_scale(self, scale):
        if not isinstance(scale, Scale):
            raise TypeError

        # Function, which accepts another function to modify temperatures according to chosen scale
        def change_temp(function):
            self.curr_temp = round(function(self.curr_temp), 2)
            self.boil_temp = round(function(self.boil_temp), 2)
            self.freeze_temp = round(function(self.freeze_temp), 2)

        if self.curr_scale == Scale.CELSIUS:
            if scale == Scale.FARENHEIT:
                change_temp(self.from_celsius_to_farenheit)
            elif scale == Scale.KELVIN:
                change_temp(self.from_celsius_to_kelvin)
        elif self.curr_scale == Scale.FARENHEIT:
            if scale == Scale.CELSIUS:
                change_temp(self.from_farenheit_to_celsius)
            elif scale == Scale.KELVIN:
                change_temp(self.from_farenheit_to_kelvin)
        else:
            if scale == Scale.CELSIUS:
                change_temp(self.from_kelvin_to_celsius)
            elif scale == Scale.FARENHEIT:
                change_temp(self.from_kelvin_to_farenheit)
        self.curr_scale = scale


# Class, which represent Chlorine element
class Chlorine(Element):
    name = "Chlorine"

    def __init__(self, init_temp):
        self.curr_temp = 0
        self.freeze_temp = -100
        self.boil_temp = -34
        self.curr_scale = Scale.CELSIUS
        self.curr_state = self.agg_state(init_temp)
        self.curr_temp = init_temp

    def __str__(self):
        return f"{self.name}, {self.curr_state.value} state. Current temperature - " \
               f"{self.curr_temp} {self.curr_scale.value}"


# Chlorine object with temperature -101
element = Chlorine(-101)
print(element)

# Change scale to Farenheit
element.swap_scale(Scale.FARENHEIT)
print(element)

# Change scale to Kelvin
element.swap_scale(Scale.KELVIN)
print(element)

# Check aggregate state
print(element.agg_state(100).value)

# Change scale to farenheit
element.swap_scale(Scale.FARENHEIT)
print(element)

# Change scale to celsius
element.swap_scale(Scale.CELSIUS)
print(element)

# Check agg state
print(element.agg_state(50).value)

#Chaneg scale to farenheit
element.swap_scale(Scale.FARENHEIT)
print(element)

# Check agg state
print(element.agg_state(-100).value)
