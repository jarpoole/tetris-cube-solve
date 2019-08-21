#
#
#
#
#
#
CC=g++

EXE=solve

CFLAGS= -c
LFLAGS=

OBJDIR=obj

OBJS= $(OBJDIR)/main.o \
		$(OBJDIR)/Model.o 


$(EXE):$(OBJS)
	mkdir -p $(OBJDIR)
	$(CC) -o $(EXE) $(OBJS) $(LFLAGS)

$(OBJDIR)/%.o : %.cpp
	mkdir -p $(OBJDIR)
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -rf $(OBJDIR)
	rm -rf $(EXE)

run:
	./$(EXE)
