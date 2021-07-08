from sys import exit

import pygame

import MathStuff as MATH
import GUICreator

StaticButton = GUICreator.StaticButton
DynamicButton = GUICreator.DynamicButton
StaticTextButton = GUICreator.StaticTextButton
DynamicTextButton = GUICreator.DynamicTextButton

class MathStuffGUI:
    """Create a GUI for my calculators."""

    def __init__(self):
        """Initialize variables."""
        pygame.init()
        self.manage_fps = pygame.time.Clock()
        self.FPS = 30

        # Initialize the screen.
        display_info = pygame.display.Info()
        max_width = display_info.current_w
        max_height = display_info.current_h
        display_ratio = max_width/max_height

        if display_ratio <= 16/9:
            x = int(max_width * 0.8)
            y = int(max_width/(16/9) * 0.8)
        else:
            x = int(max_height*(16/9) * 0.8)
            y = int(max_height * 0.8)

        self.screen = pygame.display.set_mode((x, y), pygame.RESIZABLE)
        pygame.display.set_caption("Math Stuff")
        self.screen_rect = self.screen.get_rect()
        
        self.create_all_gui()
        self.universal_menu_variables()

    def run_program(self):
        """Run the program."""
        while True:
            self.manage_fps.tick(self.FPS)
            self.get_events()
            self.update_screen()

    def universal_menu_variables(self):
        """Create flags for the menus."""
        self.active_menu = 'main_menu'
        self.active_button = ''

        self.input_box_1 = ''
        self.input_box_2 = ''
        self.input_box_3 = ''
        self.input_box_4 = ''
        self.input_box_5 = ''
        self.input_box_6 = ''
        self.input_box_7 = ''

        self.input_box_1_mod = ''
        self.input_box_2_mod = ''
        self.input_box_3_mod = ''
        self.input_box_4_mod = ''
        self.input_box_5_mod = ''
        self.input_box_6_mod = ''
        self.input_box_7_mod = ''

        self.input_value_1 = 0
        self.input_value_2 = 0
        self.input_value_3 = 0
        self.input_value_4 = 0
        self.input_value_5 = 0
        self.input_value_6 = 0
        self.input_value_7 = 0

        self.answer = ''
        self.answer_text_x_mod = 0

        self.hover_text = ''
        self.input_buttons = 0

    def reset_variables(self, menu):
        """Reset the variables and change the active menu."""
        self.active_button = ''
        self.active_menu = menu
        self.answer = ''

        self.input_box_1 = ''
        self.input_box_2 = ''
        self.input_box_3 = ''
        self.input_box_4 = ''
        self.input_box_5 = ''
        self.input_box_6 = ''
        self.input_box_7 = ''

        self.input_box_1_mod = ''
        self.input_box_2_mod = ''
        self.input_box_3_mod = ''
        self.input_box_4_mod = ''
        self.input_box_5_mod = ''
        self.input_box_6_mod = ''
        self.input_box_7_mod = ''

        self.input_value_1 = 0
        self.input_value_2 = 0
        self.input_value_3 = 0
        self.input_value_4 = 0
        self.input_value_5 = 0
        self.input_value_6 = 0
        self.input_value_7 = 0

        self.answer_text_x_mod = 0

    def event_check_number(self, event):
        """Check that the key that was pressed is valid for a number."""
        if (event.unicode == '1'
        or event.unicode == '2'
        or event.unicode == '3'
        or event.unicode == '4'
        or event.unicode == '5'
        or event.unicode == '6'
        or event.unicode == '7'
        or event.unicode == '8'
        or event.unicode == '9'
        or event.unicode == '0'
        or event.unicode == '.'
        or event.unicode == '-'):
            return True

        else:
            return False

    def event_check_letter(self, event):
        """Check that the key that was pressed is a letter."""
        if (event.unicode == 'a'
        or event.unicode == 'b'
        or event.unicode == 'c'
        or event.unicode == 'd'
        or event.unicode == 'e'
        or event.unicode == 'f'
        or event.unicode == 'g'
        or event.unicode == 'h'
        or event.unicode == 'i'
        or event.unicode == 'j'
        or event.unicode == 'k'
        or event.unicode == 'l'
        or event.unicode == 'm'
        or event.unicode == 'n'
        or event.unicode == 'o'
        or event.unicode == 'p'
        or event.unicode == 'q'
        or event.unicode == 'r'
        or event.unicode == 's'
        or event.unicode == 't'
        or event.unicode == 'u'
        or event.unicode == 'v'
        or event.unicode == 'w'
        or event.unicode == 'x'
        or event.unicode == 'y'
        or event.unicode == 'z'
        or event.unicode == 'A'
        or event.unicode == 'B'
        or event.unicode == 'C'
        or event.unicode == 'D'
        or event.unicode == 'E'
        or event.unicode == 'F'
        or event.unicode == 'G'
        or event.unicode == 'H'
        or event.unicode == 'I'
        or event.unicode == 'J'
        or event.unicode == 'K'
        or event.unicode == 'L'
        or event.unicode == 'M'
        or event.unicode == 'N'
        or event.unicode == 'O'
        or event.unicode == 'P'
        or event.unicode == 'Q'
        or event.unicode == 'R'
        or event.unicode == 'S'
        or event.unicode == 'T'
        or event.unicode == 'U'
        or event.unicode == 'V'
        or event.unicode == 'W'
        or event.unicode == 'X'
        or event.unicode == 'Y'
        or event.unicode == 'Z'):
            return True

        else:
            return False

    # Event handling.
    def get_events(self):
        """Get pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen_rect = self.screen.get_rect()
                self.create_all_gui()
            elif event.type == pygame.KEYDOWN:
                self.manage_keydown(event)
            elif event.type == pygame.KEYUP:
                self.manage_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.manage_mousebuttondown(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.manage_mousebuttonup(event)
            elif event.type == pygame.MOUSEMOTION:
                self.manage_mousemotion(event)

    def manage_mousemotion(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if (self.active_menu != 'main_menu'
            and self.active_menu != 'factors_menu'
            and self.active_menu != 'converters_menu'
            and self.active_menu != 'geometry_menu'
            and self.active_menu != 'algebra_menu'
            and self.active_menu != 'data_processing_menu'):
            if self.answer_button.button.collidepoint(mouse_pos):
                self.hover_text = 'Scroll to move the text left and right.'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.hover_text = 'Click to calculate answer, or press the enter key.'
            elif self.back_button.button.collidepoint(mouse_pos):
                self.hover_text = 'Return to previous menu.'
            elif self.hover_text_help.button.collidepoint(mouse_pos):
                self.hover_text = 'Do I need to explain everything?'
            else:
                self.hover_text = 'Hover cursor over a button for help.'

        # Get factors menu.
        if self.active_menu == 'get_factors_menu':
            if self.input_button_4.button.collidepoint(mouse_pos):
                self.hover_text = 'Enter the number you want to factor.'

        # Maintain ratio menu.
        elif self.active_menu == 'mar_menu':
            if self.input_button_1.button.collidepoint(mouse_pos):
                self.hover_text = 'Width of source surface.'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.hover_text = 'Height of source surface.'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.hover_text = 'Width of destination surface.'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.hover_text = 'Height of destination surface.'
        # Solid polygon menu.
        elif self.active_menu == 'solid_polygon_menu':
            if self.input_button_4.button.collidepoint(mouse_pos):
                self.hover_text = 'Enter the number of sides of a base.'

        # Temperature convert menu.
        elif self.active_menu == 'temp_menu':
            if self.input_button_2.button.collidepoint(mouse_pos):
                self.hover_text = 'Original temperature.'
            elif self.input_button_4.button.collidepoint(mouse_pos):
                self.hover_text = 'Current temperature scale (F, C, K).'
            elif self.input_button_6.button.collidepoint(mouse_pos):
                self.hover_text = 'Temperature scale to convert to (F, C, K).'

        # Root menu.
        elif self.active_menu == 'root_menu':
            if self.input_button_3.button.collidepoint(mouse_pos):
                self.hover_text = 'Radicand.'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.hover_text = 'Index.'
        # Extrapolate menu.
        elif self.active_menu == 'extrapolate_menu':
            if self.input_button_1.button.collidepoint(mouse_pos):
                self.hover_text = 'Start number.'
            if self.input_button_3.button.collidepoint(mouse_pos):
                self.hover_text = 'Modifier.'
            if self.input_button_5.button.collidepoint(mouse_pos):
                self.hover_text = 'Operation (Add, subtract, multiply, divide, exponent, root).'
            if self.input_button_7.button.collidepoint(mouse_pos):
                self.hover_text = 'Number of values from the start number to return.'

        # Other menus.
        elif (self.active_menu == 'common_factors_menu'
            or self.active_menu == 'gcf_menu'
            or self.active_menu == 'lcf_menu'
            or self.active_menu == 'average_menu'
            or self.active_menu == 'median_menu'
            or self.active_menu == 'mode_menu'
            or self.active_menu == 'range_menu'):
            if self.input_button_1.button.collidepoint(mouse_pos):
                self.hover_text = "First number (You don't need to use all four)."
            if self.input_button_3.button.collidepoint(mouse_pos):
                self.hover_text = "Second number (You don't need to use all four)."
            if self.input_button_5.button.collidepoint(mouse_pos):
                self.hover_text = "Third number (You don't need to use all four)."
            if self.input_button_7.button.collidepoint(mouse_pos):
                self.hover_text = "Fourth number (You don't need to use all four)."

    def manage_keydown(self, event):
        """Manage pygame KEYDOWN events."""
        if event.key == pygame.K_ESCAPE:
            exit()

        # Get factors input menu.
        elif self.active_menu == 'get_factors_input_1':
            if event.key == pygame.K_RETURN:
                if self.input_box_4 != '':
                    self.input_value_4 = int(self.input_box_4)
                    self.answer = str(MATH.get_factors_(self.input_value_4))
                    self.answer_text_x_mod = 0
                self.active_button = ''
                self.active_menu = 'get_factors_menu'
            elif event.key == pygame.K_BACKSPACE:
                self.input_box_4 = self.input_box_4[:-1]
            elif len(self.input_box_4) >= 7:
                None
            elif self.event_check_number(event):
                if (event.unicode == '-'
                    or event.unicode == '.'):
                    None
                else:
                    self.input_box_4 += event.unicode
        # Common factors input menu.
        elif (self.active_menu == 'common_factors_input_1'
            or self.active_menu == 'common_factors_input_2'
            or self.active_menu == 'common_factors_input_3'
            or self.active_menu == 'common_factors_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.common_factors_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'common_factors_menu'
                self.active_button = ''

            if self.active_menu == 'common_factors_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'common_factors_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'common_factors_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'common_factors_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode
        # Greatest common factors input menu.
        elif (self.active_menu == 'gcf_input_1'
            or self.active_menu == 'gcf_input_2'
            or self.active_menu == 'gcf_input_3'
            or self.active_menu == 'gcf_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.gcf_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'gcf_menu'
                self.active_button = ''

            if self.active_menu == 'gcf_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'gcf_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'gcf_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'gcf_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode
        # Least common factors input menu.
        elif (self.active_menu == 'lcf_input_1'
            or self.active_menu == 'lcf_input_2'
            or self.active_menu == 'lcf_input_3'
            or self.active_menu == 'lcf_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.lcf_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'lcf_menu'
                self.active_button = ''

            if self.active_menu == 'lcf_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'lcf_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'lcf_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'lcf_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode

        # Maintain ratio input menu.
        elif (self.active_menu == 'mar_input_1'
            or self.active_menu == 'mar_input_2'
            or self.active_menu == 'mar_input_3'
            or self.active_menu == 'mar_input_4'):
            if event.key == pygame.K_RETURN:
                if (self.input_box_1 == ''
                    or self.input_box_3 == ''
                    or self.input_box_5 == ''
                    or self.input_box_7 == ''):
                    None
                else:
                    self.input_value_1 = float(self.input_box_1)
                    self.input_value_3 = float(self.input_box_3)
                    self.input_value_5 = float(self.input_box_5)
                    self.input_value_7 = float(self.input_box_7)
                    source_surf = [self.input_value_1, self.input_value_3]
                    dest_surf = [self.input_value_5, self.input_value_7]
                    try:
                        self.answer = str(MATH.maintain_aspect_ratio_(
                                                    source_surf, dest_surf))
                    except ZeroDivisionError:
                        pass
                    self.answer_text_x_mod = 0
                self.active_button = ''
                self.active_menu = 'mar_menu'

            if self.active_menu == 'mar_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                    self.input_box_1_mod = self.input_box_1
                elif len(self.input_box_1_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if event.unicode == '-':
                        None
                    else:
                        self.input_box_1 += event.unicode
                        self.input_box_1_mod = self.input_box_1
                        if '.' in self.input_box_1_mod:
                            self.input_box_1_mod = self.input_box_1_mod.replace('.', '')

            elif self.active_menu == 'mar_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                    self.input_box_3_mod = self.input_box_3
                elif len(self.input_box_3_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if event.unicode == '-':
                        None
                    else:
                        self.input_box_3 += event.unicode
                        self.input_box_3_mod = self.input_box_3
                        if '.' in self.input_box_3_mod:
                            self.input_box_3_mod = self.input_box_3_mod.replace('.', '')

            elif self.active_menu == 'mar_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                    self.input_box_5_mod = self.input_box_5
                elif len(self.input_box_5_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if event.unicode == '-':
                        None
                    else:
                        self.input_box_5 += event.unicode
                        self.input_box_5_mod = self.input_box_5
                        if '.' in self.input_box_5_mod:
                            self.input_box_5_mod = self.input_box_5_mod.replace('.', '')

            elif self.active_menu == 'mar_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                    self.input_box_7_mod = self.input_box_7
                elif len(self.input_box_7_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if event.unicode == '-':
                        None
                    else:
                        self.input_box_7 += event.unicode
                        self.input_box_7_mod = self.input_box_7
                        if '.' in self.input_box_7_mod:
                            self.input_box_7_mod = self.input_box_7_mod.replace('.', '')
        # Solid polygon input menu.
        elif self.active_menu == 'solid_polygon_input_1':
            if event.key == pygame.K_RETURN:
                if self.input_box_4 != '':
                    self.input_value_4 = int(self.input_box_4)
                    self.answer = MATH.solid_polygon_info_(self.input_value_4)
                    self.answer = f'Edges = {self.answer["edges"]}, Vertices = {self.answer["vertices"]}, Faces = {self.answer["faces"]}, Triangles = {self.answer["triangles"]}'
                    self.answer_text_x_mod = 0
                self.active_button = ''
                self.active_menu = 'solid_polygon_menu'
            elif event.key == pygame.K_BACKSPACE:
                self.input_box_4 = self.input_box_4[:-1]
            elif len(self.input_box_4) >= 7:
                None
            elif self.event_check_number(event):
                if event.unicode == '-' or event.unicode == '.':
                    None
                else:
                    self.input_box_4 += event.unicode

        # Temperature convert menu.
        elif (self.active_menu == 'temp_input_1'
            or self.active_menu == 'temp_input_2'
            or self.active_menu == 'temp_input_3'):
            if event.key == pygame.K_RETURN:
                if (self.input_box_2 == ''
                    or self.input_box_4 == ''
                    or self.input_box_6 == ''):
                    None
                else:
                    self.input_value_2 = float(self.input_box_2)
                    self.input_value_4 = self.input_box_4.upper()
                    self.input_value_6 = self.input_box_6.upper()
                    self.answer = str(MATH.temperature_convert_(self.input_value_2, self.input_value_4, self.input_value_6))
                    self.answer_text_x_mod = 0
                self.active_button = ''
                self.active_menu = 'temp_menu'

            if self.active_menu == 'temp_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_2 = self.input_box_2[:-1]
                    self.input_box_2_mod = self.input_box_2
                    if '-' in self.input_box_2_mod:
                        self.input_box_2_mod = self.input_box_2_mod.replace('-', '')
                    if '.' in self.input_box_2_mod:
                        self.input_box_2_mod = self.input_box_2_mod.replace('.', '')
                elif len(self.input_box_2_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-' and '-' in self.input_box_2
                        or event.unicode == '.' and '.' in self.input_box_2):
                        None
                    else:
                        self.input_box_2 += event.unicode
                        self.input_box_2_mod = self.input_box_2
                        if '-' in self.input_box_2_mod:
                            self.input_box_2_mod = self.input_box_2_mod.replace('-', '')
                        if '.' in self.input_box_2_mod:
                            self.input_box_2_mod = self.input_box_2_mod.replace('.', '')

            elif self.active_menu == 'temp_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_4 = self.input_box_4[:-1]
                elif len(self.input_box_4) >= 1:
                    None
                elif self.event_check_letter(event):
                    if (event.unicode == 'F'
                        or event.unicode == 'f'
                        or event.unicode == 'C'
                        or event.unicode == 'c'
                        or event.unicode == 'K'
                        or event.unicode == 'k'):
                        self.input_box_4 += event.unicode

            elif self.active_menu == 'temp_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_6 = self.input_box_6[:-1]
                elif len(self.input_box_6) >= 1:
                    None
                elif self.event_check_letter(event):
                    if (event.unicode == 'F'
                        or event.unicode == 'f'
                        or event.unicode == 'C'
                        or event.unicode == 'c'
                        or event.unicode == 'K'
                        or event.unicode == 'k'):
                        self.input_box_6 += event.unicode

        # Root menu.
        elif (self.active_menu == 'root_input_1'
            or self.active_menu == 'root_input_2'):
            if event.key == pygame.K_RETURN:
                if (self.input_box_3 == ''
                    or self.input_box_5 == ''):
                    None
                else:
                    self.input_value_3 = float(self.input_box_3)
                    self.input_value_5 = float(self.input_box_5)
                    self.answer = str(MATH.root_(self.input_value_3, self.input_value_5))
                    self.answer_text_x_mod = 0
                self.active_button = ''
                self.active_menu = 'root_menu'

            if self.active_menu == 'root_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                    self.input_box_3_mod = self.input_box_3
                    if '-' in self.input_box_3_mod:
                        self.input_box_3_mod = self.input_box_3_mod.replace('-', '')
                    if '.' in self.input_box_3_mod:
                        self.input_box_3_mod = self.input_box_3_mod.replace('.', '')
                elif len(self.input_box_3_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-' and '-' in self.input_box_3
                        or event.unicode == '.' and '.' in self.input_box_3):
                        None
                    else:
                        self.input_box_3 += event.unicode
                        self.input_box_3_mod = self.input_box_3
                        if '-' in self.input_box_3_mod:
                            self.input_box_3_mod = self.input_box_3_mod.replace('-', '')
                        if '.' in self.input_box_3_mod:
                            self.input_box_3_mod = self.input_box_3_mod.replace('.', '')

            if self.active_menu == 'root_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                    self.input_box_5_mod = self.input_box_5
                    if '-' in self.input_box_5_mod:
                        self.input_box_5_mod = self.input_box_5_mod.replace('-', '')
                    if '.' in self.input_box_5_mod:
                        self.input_box_5_mod = self.input_box_5_mod.replace('.', '')
                elif len(self.input_box_5_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-' and '-' in self.input_box_5
                        or event.unicode == '.' and '.' in self.input_box_5):
                        None
                    else:
                        self.input_box_5 += event.unicode
                        self.input_box_5_mod = self.input_box_5
                        if '-' in self.input_box_5_mod:
                            self.input_box_5_mod = self.input_box_5_mod.replace('-', '')
                        if '.' in self.input_box_5_mod:
                            self.input_box_5_mod = self.input_box_5_mod.replace('.', '')
        # Extrapolate menu.
        elif (self.active_menu == 'extrapolate_input_1'
            or self.active_menu == 'extrapolate_input_2'
            or self.active_menu == 'extrapolate_input_3'
            or self.active_menu == 'extrapolate_input_4'):
            if event.key == pygame.K_RETURN:
                check = ['add', 'subtract', 'multiply', 'divide', 'exponent', 'root']
                if (self.input_box_1 == ''
                    or self.input_box_3 == ''
                    or self.input_box_5 == ''
                    or self.input_box_5.lower() not in check
                    or self.input_box_7 == ''):
                    None
                else:
                    try:
                        self.input_value_1 = int(self.input_box_1)
                        self.input_value_3 = int(self.input_box_3)
                    except ValueError:
                        self.input_value_1 = float(self.input_box_1)
                        self.input_value_3 = float(self.input_box_3)
                    self.input_value_5 = self.input_box_5.lower()
                    self.input_value_7 = int(self.input_box_7)
                    self.answer = str(MATH.extrapolate_(self.input_value_1, self.input_value_3, self.input_value_5, self.input_value_7))
                    self.answer_text_x_mod = 0
                self.active_button = ''
                self.active_menu = 'extrapolate_menu'

            if self.active_menu == 'extrapolate_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                    self.input_box_1_mod = self.input_box_1
                    if '-' in self.input_box_1_mod:
                        self.input_box_1_mod = self.input_box_1_mod.replace('-', '')
                    if '.' in self.input_box_1_mod:
                        self.input_box_1_mod = self.input_box_1_mod.replace('.', '')
                elif len(self.input_box_1_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-' and '-' in self.input_box_1
                        or event.unicode == '.' and '.' in self.input_box_1):
                        None
                    else:
                        self.input_box_1 += event.unicode
                        self.input_box_1_mod = self.input_box_1
                        if '-' in self.input_box_1_mod:
                            self.input_box_1_mod = self.input_box_1_mod.replace('-', '')
                        if '.' in self.input_box_1_mod:
                            self.input_box_1_mod = self.input_box_1_mod.replace('.', '')

            if self.active_menu == 'extrapolate_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                    self.input_box_3_mod = self.input_box_3
                    if '-' in self.input_box_3_mod:
                        self.input_box_3_mod = self.input_box_3_mod.replace('-', '')
                    if '.' in self.input_box_3_mod:
                        self.input_box_3_mod = self.input_box_3_mod.replace('.', '')
                elif len(self.input_box_3_mod) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-' and '-' in self.input_box_3
                        or event.unicode == '.' and '.' in self.input_box_3):
                        None
                    else:
                        self.input_box_3 += event.unicode
                        self.input_box_3_mod = self.input_box_3
                        if '-' in self.input_box_3_mod:
                            self.input_box_3_mod = self.input_box_3_mod.replace('-', '')
                        if '.' in self.input_box_3_mod:
                            self.input_box_3_mod = self.input_box_3_mod.replace('.', '')

            elif self.active_menu == 'extrapolate_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 8:
                    None
                elif self.event_check_letter(event):
                    self.input_box_5 += event.unicode

            elif self.active_menu == 'extrapolate_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if event.unicode == '-' or event.unicode == '.':
                        None
                    else:
                        self.input_box_7 += event.unicode

        # Average menu.
        elif (self.active_menu == 'average_input_1'
            or self.active_menu == 'average_input_2'
            or self.active_menu == 'average_input_3'
            or self.active_menu == 'average_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.average_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'average_menu'
                self.active_button = ''

            if self.active_menu == 'average_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'average_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'average_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'average_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode
        # Median menu.
        elif (self.active_menu == 'median_input_1'
            or self.active_menu == 'median_input_2'
            or self.active_menu == 'median_input_3'
            or self.active_menu == 'median_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.median_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'median_menu'
                self.active_button = ''

            if self.active_menu == 'median_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'median_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'median_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'median_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode
        # Mode menu.
        elif (self.active_menu == 'mode_input_1'
            or self.active_menu == 'mode_input_2'
            or self.active_menu == 'mode_input_3'
            or self.active_menu == 'mode_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.mode_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'mode_menu'
                self.active_button = ''

            if self.active_menu == 'mode_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'mode_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'mode_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'mode_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode
        # Range menu.
        elif (self.active_menu == 'range_input_1'
            or self.active_menu == 'range_input_2'
            or self.active_menu == 'range_input_3'
            or self.active_menu == 'range_input_4'):
            if event.key == pygame.K_RETURN:
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)
                if value_list != []:
                    self.answer = str(MATH.range_(value_list))
                    self.answer_text_x_mod = 0
                self.active_menu = 'range_menu'
                self.active_button = ''

            if self.active_menu == 'range_input_1':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_1 = self.input_box_1[:-1]
                elif len(self.input_box_1) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_1 += event.unicode

            elif self.active_menu == 'range_input_2':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_3 = self.input_box_3[:-1]
                elif len(self.input_box_3) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_3 += event.unicode

            elif self.active_menu == 'range_input_3':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_5 = self.input_box_5[:-1]
                elif len(self.input_box_5) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_5 += event.unicode

            elif self.active_menu == 'range_input_4':
                if event.key == pygame.K_BACKSPACE:
                    self.input_box_7 = self.input_box_7[:-1]
                elif len(self.input_box_7) >= 7:
                    None
                elif self.event_check_number(event):
                    if (event.unicode == '-'
                        or event.unicode == '.'):
                        None
                    else:
                        self.input_box_7 += event.unicode

    def manage_keyup(self, event):
        """Manage pygame KEYUP events."""
        None

    def manage_mousebuttondown(self, event):
        """Manage pygame MOUSEBUTTONDOWN events."""
        mouse_pos = pygame.mouse.get_pos()

        if self.active_menu == 'main_menu':
            if self.converters_button.button.collidepoint(mouse_pos):
                self.active_button = 'converters_button'
            elif self.factors_button.button.collidepoint(mouse_pos):
                self.active_button = 'factors_button'
            elif self.geometry_button.button.collidepoint(mouse_pos):
                self.active_button = 'geometry_button'
            elif self.algebra_button.button.collidepoint(mouse_pos):
                self.active_button = 'algebra_button'
            elif self.data_processing_button.button.collidepoint(mouse_pos):
                self.active_button = 'data_processing_button'

        elif (self.active_menu != 'main_menu'
        and self.active_menu != 'factors_menu'
        and self.active_menu != 'converters_menu'
        and self.active_menu != 'geometry_menu'
        and self.active_menu != 'algebra_menu'
        and self.active_menu != 'data_processing_menu'):
            if self.answer_button.button.collidepoint(mouse_pos):
                if event.button == 4:
                    self.answer_text_x_mod -= self.answer_text_move_amount
                elif event.button == 5:
                    self.answer_text_x_mod += self.answer_text_move_amount

        self.converters_menu_mousebuttondown(event, mouse_pos)

        self.factors_menu_mousebuttondown(event, mouse_pos)

        self.geometry_menu_mousebuttondown(event, mouse_pos)

        self.algebra_menu_mousebuttondown(event, mouse_pos)

        self.data_processing_menu_mousebuttondown(event, mouse_pos)

    def manage_mousebuttonup(self, event):
        """Manage pygame MOUSEBUTTONUP events."""
        mouse_pos = pygame.mouse.get_pos()

        if self.active_menu == 'main_menu':
            if self.converters_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'converters_menu'

            elif self.factors_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'factors_menu'

            elif self.geometry_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'geometry_menu'

            elif self.algebra_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'algebra_menu'

            elif self.data_processing_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'data_processing_menu'

            else:
                self.active_button = ''

        self.factors_menu_mousebuttonup(event, mouse_pos)

        self.converters_menu_mousebuttonup(event, mouse_pos)

        self.geometry_menu_mousebuttonup(event, mouse_pos)

        self.algebra_menu_mousebuttonup(event, mouse_pos)

        self.data_processing_menu_mousebuttonup(event, mouse_pos)

    def factors_menu_mousebuttondown(self, event, mouse_pos):
        """Manage the MOUSEBUTTONDOWN events for the factors menu."""
        # Main factors menu.
        if self.active_menu == 'factors_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.get_factors_button.button.collidepoint(mouse_pos):
                self.active_button = 'get_factors_button'
            elif self.common_factors_button.button.collidepoint(mouse_pos):
                self.active_button = 'common_factors_button'
            elif self.gcf_button.button.collidepoint(mouse_pos):
                self.active_button = 'gcf_button'
            elif self.lcf_button.button.collidepoint(mouse_pos):
                self.active_button = 'lcf_button'

        # Get factors menu.
        elif self.active_menu == 'get_factors_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_4.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_4'
                self.active_menu = 'get_factors_input_1'
        # Get factors input menu
        elif self.active_menu == 'get_factors_input_1':
            self.active_menu = 'get_factors_menu'
            self.active_button = ''

        # Common factors menu.
        elif self.active_menu == 'common_factors_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'common_factors_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'common_factors_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'common_factors_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'common_factors_input_4'
        # Common factors input menus
        elif self.active_menu == 'common_factors_input_1':
            self.active_menu = 'common_factors_menu'
            self.active_button = ''
        elif self.active_menu == 'common_factors_input_2':
            self.active_menu = 'common_factors_menu'
            self.active_button = ''
        elif self.active_menu == 'common_factors_input_3':
            self.active_menu = 'common_factors_menu'
            self.active_button = ''
        elif self.active_menu == 'common_factors_input_4':
            self.active_menu = 'common_factors_menu'
            self.active_button = ''

        #GCF menu.
        elif self.active_menu == 'gcf_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'gcf_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'gcf_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'gcf_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'gcf_input_4'
        # Greatest common factors input menus
        elif self.active_menu == 'gcf_input_1':
            self.active_menu = 'gcf_menu'
            self.active_button = ''
        elif self.active_menu == 'gcf_input_2':
            self.active_menu = 'gcf_menu'
            self.active_button = ''
        elif self.active_menu == 'gcf_input_3':
            self.active_menu = 'gcf_menu'
            self.active_button = ''
        elif self.active_menu == 'gcf_input_4':
            self.active_menu = 'gcf_menu'
            self.active_button = ''

        # LCF menu.
        elif self.active_menu == 'lcf_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'lcf_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'lcf_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'lcf_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'lcf_input_4'
        # Least common factors input menus
        elif self.active_menu == 'lcf_input_1':
            self.active_menu = 'lcf_menu'
            self.active_button = ''
        elif self.active_menu == 'lcf_input_2':
            self.active_menu = 'lcf_menu'
            self.active_button = ''
        elif self.active_menu == 'lcf_input_3':
            self.active_menu = 'lcf_menu'
            self.active_button = ''
        elif self.active_menu == 'lcf_input_4':
            self.active_menu = 'lcf_menu'
            self.active_button = ''

    def factors_menu_mousebuttonup(self, event, mouse_pos):
        """Manage the MOUSEBUTTONUP events for the factors menu."""
        # Main factors menu.
        if self.active_menu == 'factors_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'main_menu'
            elif self.get_factors_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'get_factors_menu'
                self.input_buttons = 1
            elif self.common_factors_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'common_factors_menu'
                self.input_buttons = 4
            elif self.gcf_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'gcf_menu'
                self.input_buttons = 4
            elif self.lcf_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'lcf_menu'
                self.input_buttons = 4

            else:
                self.active_button = ''

        # Get factors menu.
        elif self.active_menu == 'get_factors_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('factors_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                if self.input_box_4 != '':
                    self.input_value_4 = int(self.input_box_4)
                    self.answer = str(MATH.get_factors_(self.input_value_4))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # Common factors menu.
        elif self.active_menu == 'common_factors_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('factors_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.common_factors_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # GCF menu.
        elif self.active_menu == 'gcf_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('factors_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.gcf_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # LCF menu.
        elif self.active_menu == 'lcf_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('factors_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.lcf_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

    def converters_menu_mousebuttondown(self, event, mouse_pos):
        """Manage the MOUSEBUTTONDOWN events for the converters menu."""
        # Main converters menu.
        if self.active_menu == 'converters_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.temp_button.button.collidepoint(mouse_pos):
                self.active_button = 'temp_button'

        # Temperature convert menu.
        elif self.active_menu == 'temp_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button' 
            elif self.input_button_2.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_2'
                self.active_menu = 'temp_input_1'
            elif self.input_button_4.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_4'
                self.active_menu = 'temp_input_2'
            elif self.input_button_6.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_6'
                self.active_menu = 'temp_input_3'
        # Temperature input menus.
        elif self.active_menu == 'temp_input_1':
            self.active_menu = 'temp_menu'
            self.active_button = ''
        elif self.active_menu == 'temp_input_2':
            self.active_menu = 'temp_menu'
            self.active_button = ''
        elif self.active_menu == 'temp_input_3':
            self.active_menu = 'temp_menu'
            self.active_button = ''

    def converters_menu_mousebuttonup(self, event, mouse_pos):
        """Manage the MOUSEBUTTONUP events for the converters menu."""
        # Main converters menu.
        if self.active_menu == 'converters_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'main_menu'
            elif self.temp_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'temp_menu'
                self.input_buttons = 3

            else:
                self.active_button = ''

        # Temperature convert menu.
        elif self.active_menu == 'temp_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('converters_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                if (self.input_box_2 == ''
                    or self.input_box_4 == ''
                    or self.input_box_6 == ''):
                    None
                else:
                    self.input_value_2 = float(self.input_box_2)
                    self.input_value_4 = self.input_box_4.upper()
                    self.input_value_6 = self.input_box_6.upper()
                    self.answer = str(MATH.temperature_convert_(self.input_value_2, self.input_value_4, self.input_value_6))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

    def geometry_menu_mousebuttondown(self, event, mouse_pos):
        """Manage the MOUSEBUTTONDOWN events for the geometry menu."""
        # Main geometry menu.
        if self.active_menu == 'geometry_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.mar_button.button.collidepoint(mouse_pos):
                self.active_button = 'mar_button'
            elif self.solid_polygon_button.button.collidepoint(mouse_pos):
                self.active_button = 'solid_polygon_button'

        # Maintain ratio menu.
        elif self.active_menu == 'mar_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'mar_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'mar_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'mar_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'mar_input_4'
        # Maintain ratio input menus.
        elif self.active_menu == 'mar_input_1':
            self.active_menu = 'mar_menu'
            self.active_button = ''
        elif self.active_menu == 'mar_input_2':
            self.active_menu = 'mar_menu'
            self.active_button = ''
        elif self.active_menu == 'mar_input_3':
            self.active_menu = 'mar_menu'
            self.active_button = ''
        elif self.active_menu == 'mar_input_4':
            self.active_menu = 'mar_menu'
            self.active_button = ''

        # Solid polygon menu.
        elif self.active_menu == 'solid_polygon_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_4.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_4'
                self.active_menu = 'solid_polygon_input_1'
        # Solid polygon input menu.
        elif self.active_menu == 'solid_polygon_input_1':
            self.active_menu = 'solid_polygon_menu'
            self.active_button = ''

    def geometry_menu_mousebuttonup(self, event, mouse_pos):
        """Manage the MOUSEBUTTONUP events for the geometry menu."""
        # Main geometry menu.
        if self.active_menu == 'geometry_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'main_menu'
            elif self.mar_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'mar_menu'
                self.input_buttons = 4
            elif self.solid_polygon_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'solid_polygon_menu'
                self.input_buttons = 1

            else:
                self.active_button = ''

        # Maintain ratio menu.
        elif self.active_menu == 'mar_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('geometry_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                if (self.input_box_1 == ''
                    or self.input_box_3 == ''
                    or self.input_box_5 == ''
                    or self.input_box_7 == ''):
                    None
                else:
                    self.input_value_1 = float(self.input_box_1)
                    self.input_value_3 = float(self.input_box_3)
                    self.input_value_5 = float(self.input_box_5)
                    self.input_value_7 = float(self.input_box_7)
                    source_surf = [self.input_value_1, self.input_value_3]
                    dest_surf = [self.input_value_5, self.input_value_7]
                    try:
                        self.answer = str(MATH.maintain_aspect_ratio_(
                                                    source_surf, dest_surf))
                    except ZeroDivisionError:
                        pass
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # Solid polygon menu.
        elif self.active_menu == 'solid_polygon_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('geometry_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                if self.input_box_4 != '':
                    self.input_value_4 = int(self.input_box_4)
                    self.answer = MATH.solid_polygon_info_(self.input_value_4)
                    self.answer = f'Edges = {self.answer["edges"]}, Vertices = {self.answer["vertices"]}, Faces = {self.answer["faces"]}, Triangles = {self.answer["triangles"]}'
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

    def algebra_menu_mousebuttondown(self, event, mouse_pos):
        """Manage the MOUSEBUTTONDOWN events for the algebra menu."""
        # Main algebra menu.
        if self.active_menu == 'algebra_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.root_button.button.collidepoint(mouse_pos):
                self.active_button = 'root_button'
            elif self.extrapolate_button.button.collidepoint(mouse_pos):
                self.active_button = 'extrapolate_button'

        # Root menu.
        elif self.active_menu == 'root_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'root_input_1'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'root_input_2'
        # Root input menus.
        elif self.active_menu == 'root_input_1':
            self.active_menu = 'root_menu'
            self.active_button = ''
        elif self.active_menu == 'root_input_2':
            self.active_menu = 'root_menu'
            self.active_button = ''

        # Extrapolate menu.
        elif self.active_menu == 'extrapolate_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'extrapolate_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'extrapolate_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'extrapolate_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'extrapolate_input_4'
        # Extrapolate input menus.
        elif self.active_menu == 'extrapolate_input_1':
            self.active_menu = 'extrapolate_menu'
            self.active_button = ''
        elif self.active_menu == 'extrapolate_input_2':
            self.active_menu = 'extrapolate_menu'
            self.active_button = ''
        elif self.active_menu == 'extrapolate_input_3':
            self.active_menu = 'extrapolate_menu'
            self.active_button = ''
        elif self.active_menu == 'extrapolate_input_4':
            self.active_menu = 'extrapolate_menu'
            self.active_button = ''

    def algebra_menu_mousebuttonup(self, event, mouse_pos):
        """Manage the MOUSEBUTTONUP events for the algebra menu."""
        # Main algebra menu.
        if self.active_menu == 'algebra_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'main_menu'
            elif self.root_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'root_menu'
                self.input_buttons = 2
            elif self.extrapolate_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'extrapolate_menu'
                self.input_buttons = 4

            else:
                self.active_button = ''

        # Root menu.
        elif self.active_menu == 'root_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('algebra_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                if self.input_box_3 == '' or self.input_box_5 == '':
                    None
                else:
                    self.input_value_3 = float(self.input_box_3)
                    self.input_value_5 = float(self.input_box_5)
                    self.answer = str(MATH.root_(self.input_value_3, self.input_value_5))
                    self.answer_text_x_mod = 0
                self.active_button = ''

        # Extrapolate menu.
        elif self.active_menu == 'extrapolate_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('algebra_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                check = ['add', 'subtract', 'multiply', 'divide', 'exponent', 'root']
                if (self.input_box_1 == ''
                    or self.input_box_3 == ''
                    or self.input_box_5 == ''
                    or self.input_box_5.lower() not in check
                    or self.input_box_7 == ''):
                    None
                else:
                    try:
                        self.input_value_1 = int(self.input_box_1)
                        self.input_value_3 = int(self.input_box_3)
                    except ValueError:
                        self.input_value_1 = float(self.input_box_1)
                        self.input_value_3 = float(self.input_box_3)
                    self.input_value_5 = self.input_box_5.lower()
                    self.input_value_7 = int(self.input_box_7)
                    self.answer = str(MATH.extrapolate_(self.input_value_1, self.input_value_3, self.input_value_5, self.input_value_7))
                    self.answer_text_x_mod = 0
                self.active_button = ''

    def data_processing_menu_mousebuttondown(self, event, mouse_pos):
        """Manage the MOUSEBUTTONDOWN events for the data processing menu."""
        # Main data processing menu.
        if self.active_menu == 'data_processing_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.average_button.button.collidepoint(mouse_pos):
                self.active_button ='average_button'
            elif self.median_button.button.collidepoint(mouse_pos):
                self.active_button ='median_button'
            elif self.mode_button.button.collidepoint(mouse_pos):
                self.active_button ='mode_button'
            elif self.range_button.button.collidepoint(mouse_pos):
                self.active_button ='range_button'

        # Average menu.
        elif self.active_menu == 'average_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'average_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'average_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'average_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'average_input_4'
        # Average input menus.
        elif (self.active_menu == 'average_input_1'
            or self.active_menu == 'average_input_2'
            or self.active_menu == 'average_input_3'
            or self.active_menu == 'average_input_4'):
            self.active_button = ''
            self.active_menu = 'average_menu'

        # Median menu.
        elif self.active_menu == 'median_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'median_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'median_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'median_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'median_input_4'
        # Median input menus.
        elif (self.active_menu == 'median_input_1'
            or self.active_menu == 'median_input_2'
            or self.active_menu == 'median_input_3'
            or self.active_menu == 'median_input_4'):
            self.active_button = ''
            self.active_menu = 'median_menu'

        # Mode menu.
        elif self.active_menu == 'mode_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'mode_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'mode_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'mode_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'mode_input_4'
        # Mode input menus.
        elif (self.active_menu == 'mode_input_1'
            or self.active_menu == 'mode_input_2'
            or self.active_menu == 'mode_input_3'
            or self.active_menu == 'mode_input_4'):
            self.active_button = ''
            self.active_menu = 'mode_menu'

        # Range menu.
        elif self.active_menu == 'range_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = 'back_button'
            elif self.calculate_button.button.collidepoint(mouse_pos):
                self.active_button = 'calculate_button'
            elif self.input_button_1.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_1'
                self.active_menu = 'range_input_1'
            elif self.input_button_3.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_3'
                self.active_menu = 'range_input_2'
            elif self.input_button_5.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_5'
                self.active_menu = 'range_input_3'
            elif self.input_button_7.button.collidepoint(mouse_pos):
                self.active_button = 'input_button_7'
                self.active_menu = 'range_input_4'
        # Range input menus.
        elif (self.active_menu == 'range_input_1'
            or self.active_menu == 'range_input_2'
            or self.active_menu == 'range_input_3'
            or self.active_menu == 'range_input_4'):
            self.active_button = ''
            self.active_menu = 'range_menu'

    def data_processing_menu_mousebuttonup(self, event, mouse_pos):
        """Manage the MOUSEBUTTONUP events for the data processing menu."""
        # Main data processing menu.
        if self.active_menu == 'data_processing_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'main_menu'
            elif self.average_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'average_menu'
                self.input_buttons = 4
            elif self.median_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'median_menu'
                self.input_buttons = 4
            elif self.mode_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'mode_menu'
                self.input_buttons = 4
            elif self.range_button.button.collidepoint(mouse_pos):
                self.active_button = ''
                self.active_menu = 'range_menu'
                self.input_buttons = 4

            else:
                self.active_button = ''

        # Average menu.
        elif self.active_menu == 'average_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('data_processing_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.average_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # Median menu.
        elif self.active_menu == 'median_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('data_processing_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.median_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # Mode menu.
        elif self.active_menu == 'mode_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('data_processing_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.mode_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

        # Range menu.
        elif self.active_menu == 'range_menu':
            if self.back_button.button.collidepoint(mouse_pos):
                self.reset_variables('data_processing_menu')
            elif self.calculate_button.button.collidepoint(mouse_pos):
                value_list = []
                if self.input_box_1 != '':
                    self.input_value_1 = int(self.input_box_1)
                    value_list.append(self.input_value_1)
                if self.input_box_3 != '':
                    self.input_value_3 = int(self.input_box_3)
                    value_list.append(self.input_value_3)
                if self.input_box_5 != '':
                    self.input_value_5 = int(self.input_box_5)
                    value_list.append(self.input_value_5)
                if self.input_box_7 != '':
                    self.input_value_7 = int(self.input_box_7)
                    value_list.append(self.input_value_7)

                if value_list != []:
                    self.answer = str(MATH.range_(value_list))
                    self.answer_text_x_mod = 0
                self.active_button = ''

            else:
                self.active_button = ''

    # GUI section.
    def create_all_gui(self):
        """Quick call all of the button creation functions."""
        self.active_button_color = (150,150,160)
        self.idle_button_color = (210,210,220)
        self.border_color = (60,60,70)
        self.text_color = (0,0,0)

        self.width = self.screen_rect.width * 0.25
        self.height = self.screen_rect.height * 0.05
        self.x_gap = self.width * 0.2
        self.border_size = 0.18

        if self.screen_rect.width / self.screen_rect.height >= 1.4:
            self.text_size = 1.2
        elif self.screen_rect.width / self.screen_rect.height >= 1:
            self.text_size = 0.9
        elif self.screen_rect.width / self.screen_rect.height >= 0.8:
            self.text_size = 0.75
        else:
            self.text_size = 0.5

        self.answer_text_move_amount = self.screen_rect.width*0.1

        self.tiles = []
        column, row = 0, 0
        gap = int(self.screen_rect.width*0.001)
        if gap < 1:
            gap = 1

        diagonal = ((self.screen_rect.width**2 + self.screen_rect.height**2)
                                                                    **(1/2))
        size = int(diagonal/18) - gap

        x_amount = int((self.screen_rect.width/size) + 1)
        y_amount = int((self.screen_rect.height/size) + 1)
        amount = x_amount * y_amount

        for tile in range(amount):
            if column == x_amount:
                column = 0
                row += 1
            tile = StaticButton(self,
                    width=size,
                    height=size,
                    button_color=(230,230,230),
                    align='topleft',
                    align_obj=self.screen_rect.topleft,
                    add_x=int(gap + (size + gap) * column),
                    add_y=int(gap + (size + gap) * row))
            self.tiles.append(tile)
            column += 1

        self.back_button = DynamicTextButton(self,
                width=self.width/2,
                height=self.height,
                border_size=self.border_size/2,
                text_size=self.text_size,
                align='topleft',
                align_obj=self.screen_rect.topleft)

        self.calculate_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*1.5,
                border_size=self.border_size*0.75,
                height=self.height*1.25,
                multiply_y=1.68)

        self.answer_button = DynamicTextButton(self,
                text_size=self.text_size/1.5,
                width=self.screen_rect.width,
                border_size=self.border_size,
                height=self.height*1.25,
                multiply_y=1.92)

        self.hover_text_help = DynamicTextButton(self,
                width=self.width*3,
                height=self.height*1.1,
                border_size=0.17,
                text_size=self.text_size,
                multiply_y=0.175)

        self.input_button_1 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height,
                multiply_x=0.4)
        self.input_button_2 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height,
                multiply_x=0.6)
        self.input_button_3 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height,
                multiply_x=0.8)
        self.input_button_4 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height)
        self.input_button_5 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height,
                multiply_x=1.2)
        self.input_button_6 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height,
                multiply_x=1.4)
        self.input_button_7 = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width*0.62,
                border_size=self.border_size,
                height=self.height,
                multiply_x=1.6)

        self.create_main_menu_gui()
        self.create_converters_menu_gui()
        self.create_factors_menu_gui()
        self.create_geometry_menu_gui()
        self.create_algebra_menu_gui()
        self.create_data_processing_menu_gui()
    
    # Main menu.
    def create_main_menu_gui(self):
        """Create the buttons for the main menu."""
        self.converters_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.6)
        self.factors_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.8)
        self.geometry_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height)
        self.data_processing_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.2)
        self.algebra_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.4)

    def draw_main_menu_gui(self):
        """Draw the main menu."""
        if self.active_button != 'factors_button':
            self.factors_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Factors")
        elif self.active_button == 'factors_button':
            self.factors_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Factors")

        if self.active_button != 'converters_button':
            self.converters_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Converters")
        elif self.active_button == 'converters_button':
            self.converters_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Converters")

        if self.active_button != 'geometry_button':
            self.geometry_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Geometry")
        elif self.active_button == 'geometry_button':
            self.geometry_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Geometry")

        if self.active_button != 'algebra_button':
            self.algebra_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Algebra")
        elif self.active_button == 'algebra_button':
            self.algebra_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Algebra")

        if self.active_button != 'data_processing_button':
            self.data_processing_button.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Data Processing")
        elif self.active_button == 'data_processing_button':
            self.data_processing_button.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Data Processing")
    
    # Converters menu.
    def create_converters_menu_gui(self):
        """Create the buttons for the converters menu."""
        self.temp_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height)

    def draw_converters_menu_gui(self):
        """Draw the converters menu."""
        if self.active_button != 'temp_button':
            self.temp_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Temperature")
        elif self.active_button == 'temp_button':
            self.temp_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Temperature")
    
    # Factors menu.
    def create_factors_menu_gui(self):
        """Create the buttons for the factors menu."""
        self.get_factors_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.7)
        self.common_factors_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.9)
        self.gcf_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.1)
        self.lcf_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.3)

    def draw_factors_menu_gui(self):
        """Draw the factors menu."""
        if self.active_button != 'get_factors_button':
            self.get_factors_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Factoring")
        elif self.active_button == 'get_factors_button':
            self.get_factors_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Factoring")

        if self.active_button != 'common_factors_button':
             self.common_factors_button.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Common Factors")
        elif self.active_button == 'common_factors_button':
             self.common_factors_button.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Common Factors")

        if self.active_button != 'gcf_button':
            self.gcf_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="GCF")
        elif self.active_button == 'gcf_button':
            self.gcf_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="GCF")

        if self.active_button != 'lcf_button':
            self.lcf_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="LCF")
        elif self.active_button == 'lcf_button':
            self.lcf_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="LCF")

    # Geometry menu.
    def create_geometry_menu_gui(self):
        """Create the buttons for the geometry menu."""
        self.mar_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.9)
        self.solid_polygon_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.1)

    def draw_geometry_menu_gui(self):
        """Draw the geometry menu."""
        if self.active_button != 'mar_button':
            self.mar_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Maintain Ratio")
        elif self.active_button == 'mar_button':
            self.mar_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Maintain Ratio")

        if self.active_button != 'solid_polygon_button':
            self.solid_polygon_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="2D Solid Info")
        elif self.active_button == 'solid_polygon_button':
            self.solid_polygon_button.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="2D Solid Info")
    
    # Algebra menu.
    def create_algebra_menu_gui(self):
        """Create the buttons for the algebra menu."""
        self.root_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.9)
        self.extrapolate_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.1)

    def draw_algebra_menu_gui(self):
        """Draw the algebra menu."""
        if self.active_button != 'root_button':
            self.root_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Root")
        elif self.active_button == 'root_button':
            self.root_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Root")

        if self.active_button != 'extrapolate_button':
            self.extrapolate_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Extrapolate")
        elif self.active_button == 'extrapolate_button':
            self.extrapolate_button.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Extrapolate")
    
    # Data processing menu.
    def create_data_processing_menu_gui(self):
        """Create the buttons for the data processing menu."""
        self.average_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.7)
        self.median_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=0.9)
        self.mode_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.1)
        self.range_button = DynamicTextButton(self,
                text_size=self.text_size,
                width=self.width,
                border_size=self.border_size,
                height=self.height,
                multiply_y=1.3)

    def draw_data_processing_menu_gui(self):
        """Draw the data processing menu."""
        if self.active_button != 'average_button':
            self.average_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Mean/Average")
        elif self.active_button == 'average_button':
            self.average_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Mean/Average")

        if self.active_button != 'median_button':
             self.median_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Median")
        elif self.active_button == 'median_button':
             self.median_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Median")

        if self.active_button != 'mode_button':
            self.mode_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Mode")
        elif self.active_button == 'mode_button':
            self.mode_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Mode")

        if self.active_button != 'range_button':
            self.range_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Range")
        elif self.active_button == 'range_button':
            self.range_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Range")

    # Redraw all screen elements.
    def update_screen(self):
        """Update the screen."""
        self.screen.fill((60,60,60))
        for tile in self.tiles:
            tile.draw()

        if self.active_menu != 'main_menu':
            if self.active_button != 'back_button':
                self.back_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Back")
            elif self.active_button == 'back_button':
                self.back_button.draw(button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Back")

            if (self.active_menu != 'factors_menu'
            and self.active_menu != 'converters_menu'
            and self.active_menu != 'geometry_menu'
            and self.active_menu != 'algebra_menu'
            and self.active_menu != 'data_processing_menu'):
                if self.active_button != 'calculate_button':
                    self.calculate_button.draw(button_color=(30,220,30),
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Calculate [ENTER]")
                elif self.active_button == 'calculate_button':
                    self.calculate_button.draw(button_color=(20,140,20),
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text="Calculate [ENTER]")

                self.answer_button.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.answer,
                                    text_x_add=self.answer_text_x_mod)

                self.hover_text_help.draw(button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.hover_text)

                if self.input_buttons == 1:
                    if self.active_button != 'input_button_4':
                        self.input_button_4.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_4)
                    elif self.active_button == 'input_button_4':
                        self.input_button_4.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_4)

                elif self.input_buttons == 2:
                    if self.active_button != 'input_button_3':
                        self.input_button_3.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_3)
                    elif self.active_button == 'input_button_3':
                        self.input_button_3.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_3)

                    if self.active_button != 'input_button_5':
                        self.input_button_5.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_5)
                    elif self.active_button == 'input_button_5':
                        self.input_button_5.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_5)

                elif self.input_buttons == 3:
                    if self.active_button != 'input_button_2':
                        self.input_button_2.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_2)
                    elif self.active_button == 'input_button_2':
                        self.input_button_2.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_2)

                    if self.active_button != 'input_button_4':
                        self.input_button_4.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_4)
                    elif self.active_button == 'input_button_4':
                        self.input_button_4.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_4)

                    if self.active_button != 'input_button_6':
                        self.input_button_6.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_6)
                    elif self.active_button == 'input_button_6':
                        self.input_button_6.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_6)

                elif self.input_buttons == 4:
                    if self.active_button != 'input_button_1':
                        self.input_button_1.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_1)
                    elif self.active_button == 'input_button_1':
                        self.input_button_1.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_1)

                    if self.active_button != 'input_button_3':
                        self.input_button_3.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_3)
                    elif self.active_button == 'input_button_3':
                        self.input_button_3.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_3)

                    if self.active_button != 'input_button_5':
                        self.input_button_5.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_5)
                    elif self.active_button == 'input_button_5':
                        self.input_button_5.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_5)

                    if self.active_button != 'input_button_7':
                        self.input_button_7.draw(
                                    button_color=self.active_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_7)
                    elif self.active_button == 'input_button_7':
                        self.input_button_7.draw(
                                    button_color=self.idle_button_color,
                                    border_color=self.border_color,
                                    text_color=self.text_color,
                                    text=self.input_box_7)

        if self.active_menu == 'main_menu':
            self.draw_main_menu_gui()
        elif self.active_menu == 'converters_menu':
            self.draw_converters_menu_gui()
        elif self.active_menu == 'factors_menu':
            self.draw_factors_menu_gui()
        elif self.active_menu == 'geometry_menu':
            self.draw_geometry_menu_gui()
        elif self.active_menu == 'algebra_menu':
            self.draw_algebra_menu_gui()
        elif self.active_menu == 'data_processing_menu':
            self.draw_data_processing_menu_gui()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a calculator instance, and then run it.
    main = MathStuffGUI()
    main.run_program()
