
import os, urwid, ConfigParser

class Config:

    def __init__(self):
        self.home = os.path.abspath(os.path.expanduser('~'))
        defaults = \
          {
            'cfg_sn_username'       : '',
            'cfg_sn_password'       : '',
            'cfg_db_path'           : os.path.join(self.home, '.sncli'),
            'cfg_search_mode'       : 'gstyle', # gstyle/regex
            'cfg_search_tags'       : 'yes',
            'cfg_sort_mode'         : 'date',   # alpha/date
            'cfg_pinned_ontop'      : 'yes',
            'cfg_tabstop'           : '4',
            'cfg_format_strftime'   : '%Y/%m/%d',
            'cfg_format_note_title' : '[%D] %F %-N %T',

            'kb_help'           : 'h',
            'kb_quit'           : 'q',
            'kb_down'           : 'j',
            'kb_up'             : 'k',
            'kb_page_down'      : ' ',
            'kb_page_up'        : 'b',
            'kb_half_page_down' : 'ctrl d',
            'kb_half_page_up'   : 'ctrl u',
            'kb_bottom'         : 'G',
            'kb_top'            : 'g',
            'kb_view_note'      : 'enter',
            'kb_view_log'       : 'l',
            'kb_tabstop2'       : '2',
            'kb_tabstop4'       : '4',
            'kb_tabstop8'       : '8',

            'clr_default_fg'            : 'default',
            'clr_default_bg'            : 'default',
            'clr_note_focus_fg'         : 'white',
            'clr_note_focus_bg'         : 'light red',
            'clr_note_title_day_fg'     : 'light red',
            'clr_note_title_day_bg'     : 'default',
            'clr_note_title_week_fg'    : 'light green',
            'clr_note_title_week_bg'    : 'default',
            'clr_note_title_month_fg'   : 'brown',
            'clr_note_title_month_bg'   : 'default',
            'clr_note_title_year_fg'    : 'light blue',
            'clr_note_title_year_bg'    : 'default',
            'clr_note_title_ancient_fg' : 'light blue',
            'clr_note_title_ancient_bg' : 'default',
            'clr_note_date_fg'          : 'dark blue',
            'clr_note_date_bg'          : 'default',
            'clr_note_flags_fg'         : 'dark magenta',
            'clr_note_flags_bg'         : 'default',
            'clr_note_tags_fg'          : 'dark red',
            'clr_note_tags_bg'          : 'default',
            'clr_note_content_fg'       : 'default',
            'clr_note_content_bg'       : 'default',
            'clr_note_content_focus_fg' : 'white',
            'clr_note_content_focus_bg' : 'light red',
            'clr_help_focus_fg'         : 'white',
            'clr_help_focus_bg'         : 'dark gray',
            'clr_help_header_fg'        : 'dark blue',
            'clr_help_header_bg'        : 'default',
            'clr_help_config_fg'        : 'dark green',
            'clr_help_config_bg'        : 'default',
            'clr_help_value_fg'         : 'dark red',
            'clr_help_value_bg'         : 'default',
            'clr_help_descr_fg'         : 'default',
            'clr_help_descr_bg'         : 'default'
          }

        cp = ConfigParser.SafeConfigParser(defaults)
        self.configs_read = cp.read([os.path.join(self.home, '.snclirc')])

        cfg_sec = 'sncli'

        if not cp.has_section(cfg_sec):
            cp.add_section(cfg_sec)

        self.configs = \
        {
        'sn_username'       : [ cp.get(cfg_sec, 'cfg_sn_username', raw=True),       'Simplenote Username' ],
        'sn_password'       : [ cp.get(cfg_sec, 'cfg_sn_password', raw=True),       'Simplenote Password' ],
        'db_path'           : [ cp.get(cfg_sec, 'cfg_db_path'),                     'Note storage path' ],
        'search_mode'       : [ cp.get(cfg_sec, 'cfg_search_mode'),                 'Search mode' ],
        'search_tags'       : [ cp.get(cfg_sec, 'cfg_search_tags'),                 'Search tags as well' ],
        'sort_mode'         : [ cp.get(cfg_sec, 'cfg_sort_mode'),                   'Sort mode' ],
        'pinned_ontop'      : [ cp.get(cfg_sec, 'cfg_pinned_ontop'),                'Pinned at top of list' ],
        'tabstop'           : [ cp.get(cfg_sec, 'cfg_tabstop'),                     'Tabstop spaces' ],
        'format_strftime'   : [ cp.get(cfg_sec, 'cfg_format_strftime', raw=True),   'Date strftime format' ],
        'format_note_title' : [ cp.get(cfg_sec, 'cfg_format_note_title', raw=True), 'Note title format' ]
        }

        self.keybinds = \
        {
        'help'           : [ cp.get(cfg_sec, 'kb_help'),           'Help' ],
        'quit'           : [ cp.get(cfg_sec, 'kb_quit'),           'Quit' ],
        'down'           : [ cp.get(cfg_sec, 'kb_down'),           'Scroll down one line' ],
        'up'             : [ cp.get(cfg_sec, 'kb_up'),             'Scroll up one line' ],
        'page_down'      : [ cp.get(cfg_sec, 'kb_page_down'),      'Page down' ],
        'page_up'        : [ cp.get(cfg_sec, 'kb_page_up'),        'Page up' ],
        'half_page_down' : [ cp.get(cfg_sec, 'kb_half_page_down'), 'Half page down' ],
        'half_page_up'   : [ cp.get(cfg_sec, 'kb_half_page_up'),   'Half page up' ],
        'bottom'         : [ cp.get(cfg_sec, 'kb_bottom'),         'Goto bottom' ],
        'top'            : [ cp.get(cfg_sec, 'kb_top'),            'Goto top' ],
        'view_note'      : [ cp.get(cfg_sec, 'kb_view_note'),      'View note' ],
        'view_log'       : [ cp.get(cfg_sec, 'kb_view_log'),       'View log' ],
        'tabstop2'       : [ cp.get(cfg_sec, 'kb_tabstop2'),       'View with tabstop=2' ],
        'tabstop4'       : [ cp.get(cfg_sec, 'kb_tabstop4'),       'View with tabstop=4' ],
        'tabstop8'       : [ cp.get(cfg_sec, 'kb_tabstop8'),       'View with tabstop=8' ]
        }

        self.colors = \
        {
        'default_fg'            : [ cp.get(cfg_sec, 'clr_default_fg'),            'Default fg' ],
        'default_bg'            : [ cp.get(cfg_sec, 'clr_default_bg'),            'Default bg' ],
        'note_focus_fg'         : [ cp.get(cfg_sec, 'clr_note_focus_fg'),         'Note title focus fg' ],
        'note_focus_bg'         : [ cp.get(cfg_sec, 'clr_note_focus_bg'),         'Note title focus bg' ],
        'note_title_day_fg'     : [ cp.get(cfg_sec, 'clr_note_title_day_fg'),     'Day old note title fg' ],
        'note_title_day_bg'     : [ cp.get(cfg_sec, 'clr_note_title_day_bg'),     'Day old note title bg' ],
        'note_title_week_fg'    : [ cp.get(cfg_sec, 'clr_note_title_week_fg'),    'Week old note title fg' ],
        'note_title_week_bg'    : [ cp.get(cfg_sec, 'clr_note_title_week_bg'),    'Week old note title bg' ],
        'note_title_month_fg'   : [ cp.get(cfg_sec, 'clr_note_title_month_fg'),   'Month old note title fg' ],
        'note_title_month_bg'   : [ cp.get(cfg_sec, 'clr_note_title_month_bg'),   'Month old note title bg' ],
        'note_title_year_fg'    : [ cp.get(cfg_sec, 'clr_note_title_year_fg'),    'Year old note title fg' ],
        'note_title_year_bg'    : [ cp.get(cfg_sec, 'clr_note_title_year_bg'),    'Year old note title bg' ],
        'note_title_ancient_fg' : [ cp.get(cfg_sec, 'clr_note_title_ancient_fg'), 'Ancient note title fg' ],
        'note_title_ancient_bg' : [ cp.get(cfg_sec, 'clr_note_title_ancient_bg'), 'Ancient note title bg' ],
        'note_date_fg'          : [ cp.get(cfg_sec, 'clr_note_date_fg'),          'Note date fg' ],
        'note_date_bg'          : [ cp.get(cfg_sec, 'clr_note_date_bg'),          'Note date bg' ],
        'note_flags_fg'         : [ cp.get(cfg_sec, 'clr_note_flags_fg'),         'Note flags fg' ],
        'note_flags_bg'         : [ cp.get(cfg_sec, 'clr_note_flags_bg'),         'Note flags bg' ],
        'note_tags_fg'          : [ cp.get(cfg_sec, 'clr_note_tags_fg'),          'Note tags fg' ],
        'note_tags_bg'          : [ cp.get(cfg_sec, 'clr_note_tags_bg'),          'Note tags bg' ],
        'note_content_fg'       : [ cp.get(cfg_sec, 'clr_note_content_fg'),       'Note content fg' ],
        'note_content_bg'       : [ cp.get(cfg_sec, 'clr_note_content_bg'),       'Note content bg' ],
        'note_content_focus_fg' : [ cp.get(cfg_sec, 'clr_note_content_focus_fg'), 'Note content focus fg' ],
        'note_content_focus_bg' : [ cp.get(cfg_sec, 'clr_note_content_focus_bg'), 'Note content focus bg' ],
        'help_focus_fg'         : [ cp.get(cfg_sec, 'clr_help_focus_fg'),         'Help focus fg' ],
        'help_focus_bg'         : [ cp.get(cfg_sec, 'clr_help_focus_bg'),         'Help focus bg' ],
        'help_header_fg'        : [ cp.get(cfg_sec, 'clr_help_header_fg'),        'Help header fg' ],
        'help_header_bg'        : [ cp.get(cfg_sec, 'clr_help_header_bg'),        'Help header bg' ],
        'help_config_fg'        : [ cp.get(cfg_sec, 'clr_help_config_fg'),        'Help config fg' ],
        'help_config_bg'        : [ cp.get(cfg_sec, 'clr_help_config_bg'),        'Help config bg' ],
        'help_value_fg'         : [ cp.get(cfg_sec, 'clr_help_value_fg'),         'Help value fg' ],
        'help_value_bg'         : [ cp.get(cfg_sec, 'clr_help_value_bg'),         'Help value bg' ],
        'help_descr_fg'         : [ cp.get(cfg_sec, 'clr_help_descr_fg'),         'Help description fg' ],
        'help_descr_bg'         : [ cp.get(cfg_sec, 'clr_help_descr_bg'),         'Help description bg' ]
        }

    def get_config(self, name):
        return self.configs[name][0]

    def get_config_descr(self, name):
        return self.configs[name][1]

    def get_keybind(self, name):
        return self.keybinds[name][0]

    def get_keybind_descr(self, name):
        return self.keybinds[name][1]

    def get_color(self, name):
        return self.colors[name][0]

    def get_color_descr(self, name):
        return self.colors[name][1]
