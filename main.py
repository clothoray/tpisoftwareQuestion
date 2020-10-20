import sys, os, json, codecs

def revertDict( argList ):

    jsonStr = ""
    ret = [ ":".join( "\"%s\"" % x for x in argList[ -2: ] ) ]

    arr = argList[ : -2 ]
    arr.reverse()
    for x in arr:

        ret.insert( 0, "{\"%s\"" % x )

    jsonStr = ":".join( ret[ : -1 ] )
    jsonStr += ":{%s}" % ret[ -1 : ][ 0 ]

    tail = ""
    for x in arr:
        tail += "}"

    return jsonStr + tail

def digDict( argDict ):

    if argDict and type( argDict ) is dict and len( argDict.keys() ) == 1:

        k = next( iter( argDict.keys() ) )
        v = argDict[ k ]
        if type( v ) is str:
            return [ v, k ]

        else:
            l = digDict( v )
            l.append( k )
            return l

    else:
        raise Exception( "Format error" )

def main( argv ):

    fileName = "sample.json"
    fullPath = "input/" + fileName

    try:
        if os.path.isfile( fullPath ):

            try:
                content = None
                with codecs.open( fullPath, "r", "utf-8" ) as f:
                    lines = f.readlines()
                    content = "".join( [ l.strip() for l in lines ] )

                originDict = json.loads( content )
                result = revertDict( digDict( originDict ) )


                print( "result", json.loads( result ) )

            except Exception as ee:
                raise ee

        else:
            raise Exception( "Not Found json file" )

    except Exception as e:
        print( e )

if __name__ == '__main__':
    main( sys.argv )

