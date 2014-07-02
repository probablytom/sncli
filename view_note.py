
import time, urwid
import utils

class ViewNote(urwid.ListBox):

    def __init__(self, config, args):
        self.config = config
        self.note = args['note']
        super(ViewNote, self).__init__(
                  urwid.SimpleFocusListWalker(
                      self.get_note_content_as_list(
                          int(self.config.get_config('tabstop')))))

    def get_note_content_as_list(self, tabstop):
        lines = []
        for l in self.note['content'].split('\n'):
            lines.append(
                urwid.AttrMap(urwid.Text(l.replace('\t', ' ' * tabstop)),
                              'note_content',
                              'note_content_focus'))
        return lines

    def get_status_bar(self):
        cur   = -1
        total = 0
        if len(self.body.positions()) > 0:
            cur   = self.focus_position
            total = len(self.body.positions())

        t = time.localtime(float(self.note['modifydate']))
        mod_time = time.strftime('%a, %d %b %Y %H:%M:%S', t)
        tags = '%s' % ','.join(self.note['tags'])
        status_title = \
            urwid.AttrMap(urwid.Text(u'Title: ' +
                                     utils.get_note_title(self.note),
                                     wrap='clip'),
                          'status_bar')
        status_index = \
            ('pack', urwid.AttrMap(urwid.Text(u' ' +
                                              str(cur + 1) +
                                              u'/' +
                                              str(total)),
                                   'status_bar'))
        status_date = \
            urwid.AttrMap(urwid.Text(u'Date: ' +
                                     mod_time,
                                     wrap='clip'),
                          'status_bar')
        status_tags = \
            ('pack', urwid.AttrMap(urwid.Text(u'[' + tags + u']'),
                                   'status_bar'))
        pile_top = urwid.Columns([ status_title, status_index ])
        pile_bottom = urwid.Columns([ status_date, status_tags ])
        return \
            urwid.AttrMap(urwid.Pile([ pile_top, pile_bottom ]),
                          'status_bar')

    def keypress(self, size, key):
        if key == self.config.get_keybind('tabstop2'):
            self.body[:] = \
                urwid.SimpleFocusListWalker(
                    self.get_note_content_as_list(2))

        elif key == self.config.get_keybind('tabstop4'):
            self.body[:] = \
                urwid.SimpleFocusListWalker(
                    self.get_note_content_as_list(4))

        elif key == self.config.get_keybind('tabstop8'):
            self.body[:] = \
                urwid.SimpleFocusListWalker(
                    self.get_note_content_as_list(8))

