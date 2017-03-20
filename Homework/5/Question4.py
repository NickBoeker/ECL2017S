def test_get_triangle_area():
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    verticies = [v1,v2,v3]
    expected = 1
    computed = get_triangle_area(verticies)
    tol = 1E-14
    success = abs(expected-computed) < tol
    msg = 'computed area={} != {} (expected)'.format(computed,expected)
    assert success,msg

def get_triangle_area(verticies):
    res = .5*abs(verticies[1][0]*verticies[2][1]-verticies[2][0]*verticies[1][1]-verticies[0][0]*verticies[2][1]+verticies[2][0]*verticies[0][1]+verticies[0][0]*verticies[1][1]-verticies[1][0]*verticies[0][1])
    return res

test_get_triangle_area()
