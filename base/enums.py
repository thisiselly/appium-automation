from enum import Enum

class WaitCondition(Enum):
    """
    Enum for different types of wait conditions.
    """
    PRESENCE = "PRESENCE"  # Wait for element presence in DOM
    CLICKABLE = "CLICKABLE"  # Wait for element to be clickable
    VISIBLE = "VISIBLE"  # Wait for element to be visible
    SELECTED = "SELECTED"  # Wait for element to be selected
    INVISIBLE = "INVISIBLE"  # Wait for element to be invisible
    PRESENCE_ALL = "PRESENCE_ALL"  # Wait for all elements to be present in DOM
    VISIBLE_ALL = "VISIBLE_ALL"  # Wait for all elements to be visible

class Direction(Enum):
    TO_LEFT = "left"
    TO_RIGHT = "right"
    TO_UP = "up"
    TO_DOWN = "down"
