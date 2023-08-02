"""
Interface for any object that can be rendered to the screen.
"""
class IDrawable:
    def draw(self, screen, color: tuple[int]) -> None:
        pass
