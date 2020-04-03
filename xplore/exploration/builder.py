import textwrap
from abc import ABC, abstractmethod

from xplore.exploration.utils import get_function_body


class Builder(ABC):
    def __init__(self):
        self.name = None
        self.title = None
        self.target = None

    @abstractmethod
    def build_name(self, name):
        self.name = name

    @abstractmethod
    def build_title(self, title):
        self.title = title


class ExplorationBuilder(Builder):
    def __init__(self):
        self.implementation = None
        self.executable = None

    @abstractmethod
    def build_implementation(self, implementation):
        self.implementation = textwrap.dedent(implementation).rstrip()

    @abstractmethod
    def build_executable(self, executable):
        self.executable = textwrap.dedent(get_function_body(executable))


class PlotableExplorationBuilder(ExplorationBuilder):
    def __init__(self):
        super(PlotableExplorationBuilder, self).__init__()
        self.plot_implementation = None
        self.plot_executable = None

    @abstractmethod
    def build_plot_implementation(self, plot_implementation):
        self.plot_implementation = textwrap.dedent(plot_implementation).rstrip()

    @abstractmethod
    def build_plot_executable(self, plot_executable):
        self.plot_executable = textwrap.dedent(get_function_body(plot_executable))


class PlotableBuilder(Builder):
    def __init__(self):
        super(PlotableBuilder, self).__init__()
        self.plot_implementation = None
        self.plot_executable = None

    @abstractmethod
    def build_plot_implementation(self, plot_implementation):
        self.plot_implementation = textwrap.dedent(plot_implementation).rstrip()

    @abstractmethod
    def build_plot_executable(self, plot_executable):
        self.plot_executable = textwrap.dedent(get_function_body(plot_executable))


class Director:
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder.build_name()
        self._builder.build_title()
        if isinstance(self._builder, ExplorationBuilder):
            self._builder.build_implementation()
            self._builder.build_executable()
        if isinstance(self._builder, PlotableExplorationBuilder) or isinstance(
            self._builder, PlotableBuilder
        ):
            self._builder.build_plot_implementation()
            self._builder.build_plot_executable()
        return self._builder
