"""
Interface for any object that can be rendered to the screen.
"""
class IDrawable:
    """
    Implementations of this method will draw to the screen using the provided color for lines.
    """
    def draw(self, screen, color: tuple[int]) -> None:
        pass
