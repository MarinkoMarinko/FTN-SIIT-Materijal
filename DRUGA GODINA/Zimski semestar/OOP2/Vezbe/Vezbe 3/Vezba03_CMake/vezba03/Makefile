# Standalone GNU Make alternative: no CMake or Visual Studio required.
# Intended compilation failures must be fixed in the calculator source files.

CXX ?= c++
CPPFLAGS ?=
CXXFLAGS ?= -std=c++17 -g -O0 -Wall -Wextra -Wpedantic
LDFLAGS ?=
LDLIBS ?=
OUT := build-make

.PHONY: all simple advanced clean help

all: simple advanced

simple: $(OUT)/simple_calculator
advanced: $(OUT)/advanced_calculator

$(OUT)/simple_calculator: SimpleCalculator/calculator02buggy.cpp SimpleCalculator/std_lib_facilities.h
	@mkdir -p $(OUT)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $< $(LDFLAGS) $(LDLIBS) -o $@

$(OUT)/advanced_calculator: AdvancedCalculator/calculator08buggy.cpp AdvancedCalculator/std_lib_facilities.h
	@mkdir -p $(OUT)
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $< $(LDFLAGS) $(LDLIBS) -o $@

clean:
	rm -rf $(OUT)

help:
	@echo 'make simple      # compile simple calculator'
	@echo 'make advanced    # compile advanced calculator'
	@echo 'make            # compile both'
	@echo 'make clean      # remove GNU Make outputs'
	@echo 'make CXX=clang++ simple # select Clang instead of GCC'
