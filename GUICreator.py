import pygame.font

class StaticButton:
    """Create a static button object."""

    def __init__(self, main, width, height, button_color,
                border_color=None, border_size=None,
                align=None, align_obj=None, add_x=None, add_y=None,
                multiply_x=None, multiply_y=None):
        """Initialize StaticTextButton variables."""
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.width = int(width)
        self.height = int(height)
        self.border_size = border_size
        self.button_color = button_color
        self.border_color = border_color

        self.align = align
        self.align_obj = align_obj
        self.add_x = add_x
        self.add_y = add_y
        self.multiply_x = multiply_x
        self.multiply_y = multiply_y

        self.configure_button() # Make the button.
        if self.border_size != None:
            self.configure_border() # Make the border if it's been configured.

    def configure_button(self):
        """Configure the button."""
        self.button = pygame.Rect(0,0, self.width,self.height)

        # Snap the button to another object.
        if self.align == None:
            self.button.center = self.screen_rect.center
        elif self.align == 'midright':
            self.button.midright = self.align_obj
        elif self.align == 'midleft':
            self.button.midleft = self.align_obj
        elif self.align == 'midtop':
            self.button.midtop = self.align_obj
        elif self.align == 'midbottom':
            self.button.midbottom = self.align_obj
        elif self.align == 'topleft':
            self.button.topleft = self.align_obj
        elif self.align == 'topright':
            self.button.topright = self.align_obj
        elif self.align == 'bottomright':
            self.button.bottomright = self.align_obj
        elif self.align == 'bottomleft':
            self.button.bottomleft = self.align_obj

        # Adjust the button's x or y values.
        if self.add_x != None:
            self.button.x += self.add_x
        if self.add_y != None:
            self.button.y += self.add_y
        if self.multiply_x != None:
            self.button.x *= self.multiply_x
        if self.multiply_y != None:
            self.button.y *= self.multiply_y

    def configure_border(self):
        """Configure the border."""
        self.border = pygame.Rect(0,0, self.width,self.height)

        # Make sure the border is even on both axes.
        border_size = int(self.button.height*self.border_size)
        even_check = border_size%2
        if even_check == 0:
            None
        elif even_check == 1:
            border_size += 1

        self.border.height += border_size
        self.border.width += border_size
        self.border.center = self.button.center

    def draw(self):
        """Draw the button."""
        if self.border_size != None:
            self.screen.fill(self.border_color, self.border)
        self.screen.fill(self.button_color, self.button)

class DynamicButton:
    """Create a dynamic button object."""

    def __init__(self, main, width, height, border_size=None,
                align=None, align_obj=None, add_x=None, add_y=None,
                multiply_x=None, multiply_y=None):
        """Initialize StaticTextButton variables."""
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.width = int(width)
        self.height = int(height)
        self.border_size = border_size

        self.align = align
        self.align_obj = align_obj
        self.add_x = add_x
        self.add_y = add_y
        self.multiply_x = multiply_x
        self.multiply_y = multiply_y

        self.configure_button() # Make the button.
        if self.border_size != None:
            self.configure_border() # Make the border if it's been configured.

    def configure_button(self):
        """Configure the button."""
        self.button = pygame.Rect(0,0, self.width,self.height)

        # Snap the button to another object.
        if self.align == None:
            self.button.center = self.screen_rect.center
        elif self.align == 'midright':
            self.button.midright = self.align_obj
        elif self.align == 'midleft':
            self.button.midleft = self.align_obj
        elif self.align == 'midtop':
            self.button.midtop = self.align_obj
        elif self.align == 'midbottom':
            self.button.midbottom = self.align_obj
        elif self.align == 'topleft':
            self.button.topleft = self.align_obj
        elif self.align == 'topright':
            self.button.topright = self.align_obj
        elif self.align == 'bottomright':
            self.button.bottomright = self.align_obj
        elif self.align == 'bottomleft':
            self.button.bottomleft = self.align_obj

        # Adjust the button's x or y values.
        if self.add_x != None:
            self.button.x += self.add_x
        if self.add_y != None:
            self.button.y += self.add_y
        if self.multiply_x != None:
            self.button.x *= self.multiply_x
        if self.multiply_y != None:
            self.button.y *= self.multiply_y

    def configure_border(self):
        """Configure the border."""
        self.border = pygame.Rect(0,0, self.width,self.height)

        # Make sure the border is even on both axes.
        border_size = int(self.button.height * self.border_size)
        even_check = border_size%2
        if even_check == 0:
            None
        elif even_check == 1:
            border_size += 1

        self.border.height += border_size
        self.border.width += border_size
        self.border.center = self.button.center

    def draw(self, button_color, border_color):
        """Draw the button."""
        if border_color != None:
            self.screen.fill(border_color, self.border)
        self.screen.fill(button_color, self.button)

class StaticTextButton:
    """Create a static text button object."""

    def __init__(self, main, width, height, text, text_size, button_color,
                text_color, border_color=None, border_size=None,
                align=None, align_obj=None, add_x=None, add_y=None,
                multiply_x=None, multiply_y=None):
        """Initialize StaticTextButton variables."""
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.width = int(width)
        self.height = int(height)
        self.text = text
        self.border_size = border_size
        self.button_color = button_color
        self.text_color = text_color
        self.border_color = border_color

        self.align = align
        self.align_obj = align_obj
        self.add_x = add_x
        self.add_y = add_y
        self.multiply_x = multiply_x
        self.multiply_y = multiply_y

        font_size = int(self.height*text_size)
        self.font = pygame.font.Font(None, font_size)

        self.configure_button() # Make the button.
        self.configure_text() # Make the text box.
        if self.border_size != None:
            self.configure_border() # Make the border if it's been configured.

    def configure_button(self):
        """Configure the button."""
        self.button = pygame.Rect(0,0, self.width,self.height)

        # Snap the button to another object.
        if self.align == None:
            self.button.center = self.screen_rect.center
        elif self.align == 'midright':
            self.button.midright = self.align_obj
        elif self.align == 'midleft':
            self.button.midleft = self.align_obj
        elif self.align == 'midtop':
            self.button.midtop = self.align_obj
        elif self.align == 'midbottom':
            self.button.midbottom = self.align_obj
        elif self.align == 'topleft':
            self.button.topleft = self.align_obj
        elif self.align == 'topright':
            self.button.topright = self.align_obj
        elif self.align == 'bottomright':
            self.button.bottomright = self.align_obj
        elif self.align == 'bottomleft':
            self.button.bottomleft = self.align_obj

        # Adjust the button's x or y values.
        if self.add_x != None:
            self.button.x += self.add_x
        if self.add_y != None:
            self.button.y += self.add_y
        if self.multiply_x != None:
            self.button.x *= self.multiply_x
        if self.multiply_y != None:
            self.button.y *= self.multiply_y

    def configure_border(self):
        """Configure the border."""
        self.border = pygame.Rect(0,0, self.width,self.height)

        # Make sure the border is even on both axes.
        border_size = int(self.button.height*self.border_size)
        even_check = border_size%2
        if even_check == 0:
            None
        elif even_check == 1:
            border_size += 1

        self.border.height += border_size
        self.border.width += border_size
        self.border.center = self.button.center

    def configure_text(self):
        """Configure the text."""
        self.text_image = self.font.render(self.text, True, self.text_color,
                                                            self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.button.center

    def draw(self):
        """Draw the button."""
        if self.border_color != None:
            self.screen.fill(self.border_color, self.border)
        self.screen.fill(self.button_color, self.button)
        self.screen.blit(self.text_image, self.text_image_rect)

class DynamicTextButton:
    """Create a dynamic text button object."""

    def __init__(self, main, width, height, text_size, border_size=None,
                align=None, align_obj=None, add_x=None, add_y=None,
                multiply_x=None, multiply_y=None):
        """Initialize DynamicTextButton variables."""
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.width = int(width)
        self.height = int(height)
        self.border_size = border_size

        self.align = align
        self.align_obj = align_obj
        self.add_x = add_x
        self.add_y = add_y
        self.multiply_x = multiply_x
        self.multiply_y = multiply_y

        font_size = int(self.height*text_size)
        self.font = pygame.font.Font(None, font_size)

        self.configure_button() # Make the button.
        if self.border_size != None:
            self.configure_border() # Make the border if it's been configured.

    def configure_button(self):
        """Configure the button."""
        self.button = pygame.Rect(0,0, self.width,self.height)

        # Snap the button to another object.
        if self.align == None:
            self.button.center = self.screen_rect.center
        elif self.align == 'midright':
            self.button.midright = self.align_obj
        elif self.align == 'midleft':
            self.button.midleft = self.align_obj
        elif self.align == 'midtop':
            self.button.midtop = self.align_obj
        elif self.align == 'midbottom':
            self.button.midbottom = self.align_obj
        elif self.align == 'topleft':
            self.button.topleft = self.align_obj
        elif self.align == 'topright':
            self.button.topright = self.align_obj
        elif self.align == 'bottomright':
            self.button.bottomright = self.align_obj
        elif self.align == 'bottomleft':
            self.button.bottomleft = self.align_obj

        # Adjust the button's x or y values.
        if self.add_x != None:
            self.button.x += self.add_x
        if self.add_y != None:
            self.button.y += self.add_y
        if self.multiply_x != None:
            self.button.x *= self.multiply_x
        if self.multiply_y != None:
            self.button.y *= self.multiply_y

    def configure_border(self):
        """Configure the border."""
        self.border = pygame.Rect(0,0, self.width,self.height)

        # Make sure the border is even on both axes.
        border_size = int(self.button.height*self.border_size)
        even_check = border_size%2
        if even_check == 0:
            None
        elif even_check == 1:
            border_size += 1

        self.border.height += border_size
        self.border.width += border_size
        self.border.center = self.button.center

    def draw(self, button_color, text, text_color, border_color=None,
            text_x_add=None, text_y_add=None):
        """Draw the button."""
        text_image = self.font.render(text, True, text_color, button_color)
        text_image_rect = text_image.get_rect()
        text_image_rect.center = self.button.center
        if text_x_add != None:
            text_image_rect.x += text_x_add
        if text_y_add != None:
            text_image_rect.y += text_y_add

        if border_color != None:
            self.screen.fill(border_color, self.border)
        self.screen.fill(button_color, self.button)
        self.screen.blit(text_image, text_image_rect)

class ImageButton:
    """Create an image button."""

    def __init__(self, main, width, height, button_color, image,
                alpha, keep_ratio, smooth_scale, border_size=None,
                border_color=None, align=None, align_obj=None, add_x=None,
                add_y=None, multiply_x=None, multiply_y=None, image_size=None):
        """Initialize ImageButton variables."""
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.width = int(width)
        self.height = int(height)
        self.button_color = button_color

        self.image = image
        if image_size == None:
            self.image_size = 1
        else:
            self.image_size = image_size
        self.alpha = alpha
        self.keep_ratio = keep_ratio
        self.smooth_scale = smooth_scale

        self.border_size = border_size
        self.border_color = border_color

        self.align = align
        self.align_obj = align_obj
        self.add_x = add_x
        self.add_y = add_y
        self.multiply_x = multiply_x
        self.multiply_y = multiply_y

        self.configure_button() # Make the button.
        self.configure_image() # Configure the image.
        if self.border_size != None:
            self.configure_border() # Make the border if it's been configured.

    def configure_button(self):
        """Configure the button."""
        self.button = pygame.Rect(0,0, self.width,self.height)

        # Snap the button to another object.
        if self.align == None:
            self.button.center = self.screen_rect.center
        elif self.align == 'midright':
            self.button.midright = self.align_obj
        elif self.align == 'midleft':
            self.button.midleft = self.align_obj
        elif self.align == 'midtop':
            self.button.midtop = self.align_obj
        elif self.align == 'midbottom':
            self.button.midbottom = self.align_obj
        elif self.align == 'topleft':
            self.button.topleft = self.align_obj
        elif self.align == 'topright':
            self.button.topright = self.align_obj
        elif self.align == 'bottomright':
            self.button.bottomright = self.align_obj
        elif self.align == 'bottomleft':
            self.button.bottomleft = self.align_obj

        # Adjust the button's x or y values.
        if self.add_x != None:
            self.button.x += self.add_x
        if self.add_y != None:
            self.button.y += self.add_y
        if self.multiply_x != None:
            self.button.x *= self.multiply_x
        if self.multiply_y != None:
            self.button.y *= self.multiply_y

    def configure_image(self):
        """Configure the image."""
        if self.alpha:
            self.image = pygame.image.load(self.image).convert_alpha()
        else:
            self.image = pygame.image.load(self.image).convert()

        self.image_rect = self.image.get_rect()

        if self.keep_ratio:
            image_ratio = self.image_rect.width / self.image_rect.height
            button_ratio = self.width / self.height

            if image_ratio > button_ratio:
                x = int(self.width * self.image_size)
                y = int(self.width / image_ratio * self.image_size)

            elif image_ratio < button_ratio:
                x = int(self.height * image_ratio * self.image_size)
                y = int(self.height * self.image_size)

            else:
                x = int(self.width * self.image_size)
                y = int(self.height * self.image_size)
        else:
            x = int(self.width * self.image_size)
            y = int(self.height * self.image_size)

        if self.smooth_scale:
            self.image = pygame.transform.smoothscale(self.image, (x, y))
        else:
            self.image = pygame.transform.scale(self.image, (x, y))

        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.button.center

    def configure_border(self):
        """Configure the border."""
        self.border = pygame.Rect(0,0, self.width,self.height)

        # Make sure the border is even on both axes.
        border_size = int(self.button.height*self.border_size)
        even_check = border_size%2
        if even_check == 0:
            None
        elif even_check == 1:
            border_size += 1

        self.border.height += border_size
        self.border.width += border_size
        self.border.center = self.button.center

    def draw(self):
        """Draw the button."""
        if self.border_size != None:
            self.screen.fill(self.border_color, self.border)
        self.screen.fill(self.button_color, self.button)
        self.screen.blit(self.image, self.image_rect)
